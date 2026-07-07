from services.embeddings.factory import EmbeddingFactory

def main():
    embedding_provider = EmbeddingFactory.create()

    embedding_model = embedding_provider.get_embedding_model()

    print(type(embedding_model))


if __name__ == "__main__":
    main()