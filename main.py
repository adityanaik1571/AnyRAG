from services.llm.factory import LLMFactory
def main():
    llm = LLMFactory.create()
    response = llm.invoke(
        "In one sentence, what is Retrieval-Augmented Generation?")
    print(response)
if __name__ == "__main__":
    main()