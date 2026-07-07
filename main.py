from services.loaders.providers.pdf_loader import PDFLoader
from services.splitters.factory import SplitterFactory
from services.splitters.strategies.recursive_splitter import RecursiveSplitter
from services.loaders.factory import LoaderFactory

def main():
    loader = LoaderFactory.create("data/sample-2.pdf")
    documents = loader.load()
    splitter= SplitterFactory.create()
    chunks = splitter.split(documents)
    print(f"Original documents: {len(documents)}")
    print(f"Chunks created: {len(chunks)}")
    first_chunk = chunks[0]

    print("\nMetadata:")
    print(first_chunk.metadata)

    print("\nContent Preview:")
    print(first_chunk.page_content[:300])


if __name__ == "__main__":
    main()