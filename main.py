from services.rag.ingestion_service import IngestionService
from services.rag.query_service import QueryService

def main():
    ingestion_service = IngestionService()
    ingestion_service.ingest("file path here")
    query_service = QueryService()
    results = query_service.ask("Ask your question")
    print(results)

if __name__ == "__main__":
    main()