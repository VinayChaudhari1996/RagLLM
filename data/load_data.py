import logging
# from langchain_experimental import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path):
    """Load and split the PDF document."""
    try:
        loader = PyPDFLoader(pdf_path)
        pages = loader.load_and_split()
        logging.info(f"Loaded and split PDF: {pdf_path}")
        return pages
    except Exception as e:
        logging.error(f"Error loading PDF: {e}")
        raise
