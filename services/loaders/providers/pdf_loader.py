from core.logger import get_logger
from services.loaders.base import BaseLoader
from langchain_core.documents import Document
from typing import List
from langchain_community.document_loaders import PyPDFLoader

logger = get_logger(__name__)

class PDFLoader(BaseLoader):
    """Loads PDF files into LangChain Document objects."""
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> List[Document]:
        """Load a PDF and return its pages as Document objects."""
        logger.info(f"Loading pdf file: {self.file_path}")
        loader = PyPDFLoader(file_path=self.file_path)
        documents = loader.load()
        logger.info(f"Successfully loaded {len(documents)} pages from '{self.file_path}'.")
        return documents
