from services.embeddings.factory import EmbeddingFactory
from services.loaders.factory import LoaderFactory
from services.splitters.factory import SplitterFactory
from services.vectorstores.factory import VectorStoreFactory
from core.logger import get_logger

logger = get_logger(__name__)

class IngestionService:
    def __init__(self):
        embedding_provider = EmbeddingFactory.create()
        embedding_model = embedding_provider.get_embedding_model()
        self.vector_store = VectorStoreFactory.create(embedding_model=embedding_model)

    def ingest(self, file_paths: list[str]) -> None:
        self.vector_store.reset()
        splitter = SplitterFactory.create()
        for file_path in file_paths:
            logger.info(f"Ingesting document: {file_path}")
            loader = LoaderFactory.create(file_path=file_path)
            logger.info("Loading documents...")
            documents = loader.load()
            logger.info("Splitting documents...")
            chunks = splitter.split(documents)
            logger.info(f"Storing {len(chunks)} chunks...")
            self.vector_store.store(chunks)


