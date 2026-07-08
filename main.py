from services.embeddings.factory import EmbeddingFactory
from services.loaders.factory import LoaderFactory
from services.splitters.factory import SplitterFactory
from services.vectorstores.factory import VectorStoreFactory

loader = LoaderFactory.create("store data path")
documents = loader.load()
splitter = SplitterFactory.create()
chunks = splitter.split(documents)
embedding_provider = EmbeddingFactory.create()
embedding_model = embedding_provider.get_embedding_model()
vector_store = VectorStoreFactory.create(embedding_model)
vector_store.store(chunks)
results = vector_store.retrieve(
    "The query"
)
