from services.loaders.providers.pdf_loader import PDFLoader

def main():
    loader = PDFLoader("data/sample.pdf")
    documents = loader.load()
    print(f"Loaded {len(documents)} pages.\n")
    first_page = documents[0]
    print("Metadata:")
    print(first_page.metadata)
    print("\nContent Preview:")
    print(first_page.page_content[:300])

if __name__ == "__main__":
    main()