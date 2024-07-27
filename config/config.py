import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


# PDF_FILE_PATH
PDF_FILE_PATH = os.getenv('PDF_FILE_PATH')

