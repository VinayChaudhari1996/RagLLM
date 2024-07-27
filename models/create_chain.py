import logging

from langchain_community.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI

def create_vectorstore(pages):
    """Create a FAISS vector store from the PDF pages."""
    try:
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(pages, embedding=embeddings)
        logging.info("Vectorstore created successfully")
        return vectorstore
    except Exception as e:
        logging.error(f"Error creating vectorstore: {e}")
        raise

def create_conversation_chain(vectorstore):
    """Create a conversational retrieval chain."""
    try:
        llm = ChatOpenAI(temperature=0.9, model_name="gpt-4o-mini")
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
        logging.info("Conversational chain created successfully")
        return conversation_chain
    except Exception as e:
        logging.error(f"Error creating conversation chain: {e}")
        raise
