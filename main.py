from services.rag.ingestion_service import IngestionService
from services.rag.query_service import QueryService

def main():
    ingestion_service = IngestionService()
    ingestion_service.ingest("file path")
    query_service = QueryService()
    while True:
        question = input("Ask a Question: ")
        if question.lower() == "exit":
            print("Bye!")
            break
        answer = query_service.ask(question)
        print(answer)

if __name__ == "__main__":
    main()