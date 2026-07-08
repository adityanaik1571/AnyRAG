from services.rag.ingestion_service import IngestionService
from services.rag.query_service import QueryService

def main():
    ingestion_service = IngestionService()
    ingestion_service.ingest("Data file Path")

    query_service = QueryService()
    results = query_service.ask("Any Question")

    print(results[0].page_content)

if __name__ == "__main__":
    main()