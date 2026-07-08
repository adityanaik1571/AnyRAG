from core.logger import get_logger
from typing import List
from services.vectorstore.base import BaseVectorStore
from config.settings import settings

logger = get_logger(__name__)

class ChromaVectorStoreProvider(BaseVectorStore):
    def __init__(self):
        self.embedding_model = settings.embedding_model
        self.collection_name = settings.collection_name