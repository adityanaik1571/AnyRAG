from langchain_text_splitters import RecursiveCharacterTextSplitter
from core.logger import get_logger
from config.settings import settings
from services.splitters.base import BaseSplitter
from typing import List
from langchain_core.documents import Document

logger = get_logger(__name__)
class RecursiveSplitter(BaseSplitter):
    def split(self, documents: List[Document]) -> List[Document]:
        logger.info(f"Splitting documents now...")
        splitter = RecursiveCharacterTextSplitter(chunk_size=settings.chunk_size,
                                                  chunk_overlap=settings.chunk_overlap,
                                                  length_function=len)
        chunks = splitter.split_documents(documents)
        logger.info(f"Created {len(chunks)} chunks")
        return chunks

