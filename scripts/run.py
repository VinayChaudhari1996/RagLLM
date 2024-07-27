import os
import logging
import json
from config import OPENAI_API_KEY, PDF_FILE_PATH
from data.load_data import load_pdf
from models.create_chain import create_vectorstore, create_conversation_chain

def setup_openai_api(api_key):
    """Set the OpenAI API key as an environment variable."""
    try:
        os.environ["OPENAI_API_KEY"] = api_key
        if os.getenv("OPENAI_API_KEY") == api_key:
            logging.info("OPENAI_API_KEY has been set!")
        else:
            raise ValueError("Failed to set OPENAI_API_KEY")
    except Exception as e:
        logging.error(f"Error setting API key: {e}")
        raise

def process_questions(conversation_chain, questions):
    """Process a list of questions and return a JSON blob with answers."""
    responses = []
    for question in questions:
        response = conversation_chain.run(input_text=question)
        answer = response.get('text', 'Data Not Available')
        
        # Check for low-confidence answers (using a hypothetical confidence score threshold)
        confidence_score = response.get('confidence_score', 1.0)  # Assume a confidence score is returned
        if confidence_score < 0.7:
            answer = "Data Not Available"
        
        responses.append({"question": question, "answer": answer})
    return responses

def main():
    logging.basicConfig(filename=r'app.log', level=logging.INFO)
    
    setup_openai_api(OPENAI_API_KEY)
    pages = load_pdf(PDF_FILE_PATH)
    vectorstore = create_vectorstore(pages)
    conversation_chain = create_conversation_chain(vectorstore)
    
    # Defined questions
    questions = [
        "What is the name of the company?",
        "Who is the CEO of the company?",
        "What is their vacation policy?",
        "What is the termination policy?"
    ]
    
    responses = process_questions(conversation_chain, questions)
    
    # Output the responses as JSON
    output_json = json.dumps(responses, indent=2)
    print(output_json)

if __name__ == "__main__":
    main()
