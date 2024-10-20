# PDF Q&A Slack Bot using LLM + RAG

## Overview
An intelligent Q&A system that processes PDF documents using LangChain and OpenAI's GPT models, providing automated responses through Slack integration. The system uses document embeddings and vector storage for efficient information retrieval.

## Architecture 
![image](https://github.com/user-attachments/assets/e74db7e2-1302-4745-b108-8c63ec3a07c1)

> Live Demo Screenshot
![image](https://github.com/user-attachments/assets/dfd6695b-d1f5-44c1-b24e-9fceb74ed44e)


## 🌟 Features
- 📄 PDF document processing
- 🤖 GPT-4 powered responses
- 🔍 Semantic search using FAISS
- 💾 Conversation memory
- 📱 Slack integration
- 🔄 Vector-based retrieval
- 🧠 Context-aware responses

## 🛠️ Technical Architecture

### Components
1. **Document Processing**
   - PDF loading with PyPDFLoader
   - Text splitting for optimal processing

2. **Embedding System**
   - OpenAI embeddings
   - FAISS vector store

3. **Language Model**
   - OpenAI GPT-4
   - Conversational retrieval chain

4. **Memory System**
   - Conversation buffer memory
   - Message history tracking

5. **Integration**
   - Slack webhook integration
   - JSON response formatting

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- Slack webhook URL
- Required Python packages

## 📦 Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Dependencies
```
langchain
langchain-community
langchain-openai
faiss-cpu
pypdf
requests
python-dotenv
```

## ⚙️ Configuration

1. Set up OpenAI API:
```python
import os
api_key = "YOUR-OPENAI-API-KEY"
os.environ["OPENAI_API_KEY"] = api_key
```

2. Configure Slack webhook:
```python
webhook_url = "YOUR-SLACK-WEBHOOK-URL"
```

## 🚀 Usage

### 1. Document Loading
```python
from langchain_community.document_loaders import PyPDFLoader

pdf_file_path = 'path/to/your/document.pdf'
loader = PyPDFLoader(pdf_file_path)
pages = loader.load_and_split()
```

### 2. Setting up Embeddings
```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(pages, embedding=embeddings)
```

### 3. Creating the Conversation Chain
```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0.8, model_name="gpt-4")
memory = ConversationBufferMemory(
    memory_key='chat_history',
    return_messages=True
)

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    memory=memory
)
```

### 4. Query Function
```python
def call_llm(query):
    result = conversation_chain({"question": query})
    answer = result["answer"]
    return {
        "question": query,
        "answer": answer
    }
```

### 5. Slack Integration
```python
import requests
import json

def send_to_slack(query, answer, webhook_url):
    payload = {
        'text': 'New Q&A',
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': query
                }
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': answer
                }
            }
        ]
    }
    
    response = requests.post(
        webhook_url,
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
    return response.status_code == 200
```

## 🔧 System Configuration

### Environment Variables
Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key
SLACK_WEBHOOK_URL=your_slack_webhook_url
```

## 📊 Performance Considerations

1. **Vector Store Optimization**
   - FAISS index size
   - Document chunking strategy
   - Embedding dimension

2. **Memory Management**
   - Conversation history length
   - Buffer clearing strategy

3. **Rate Limiting**
   - OpenAI API limits
   - Slack API limits

## 🔒 Security Best Practices

1. **API Key Management**
   - Use environment variables
   - Rotate keys regularly
   - Never commit keys to version control

2. **Data Handling**
   - Sanitize input queries
   - Validate webhook URLs
   - Handle sensitive information appropriately

## 🐛 Troubleshooting

Common issues and solutions:

1. **OpenAI API Issues**
   - Check API key validity
   - Verify rate limits
   - Monitor usage quotas

2. **Slack Integration Issues**
   - Validate webhook URL
   - Check payload format
   - Monitor Slack app settings

3. **PDF Processing Issues**
   - Check file permissions
   - Verify PDF format
   - Monitor memory usage

## 📈 Future Improvements

1. **Features**
   - Multiple PDF support
   - Advanced query preprocessing
   - Custom response templates

2. **Integration**
   - Additional chat platforms
   - Database storage
   - User authentication

## 🤝 Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License
MIT

## 🙏 Acknowledgments
- LangChain team
- OpenAI
- FAISS developers
- Slack platform team

## 📞 Support
For issues or questions: crate Github issues.
