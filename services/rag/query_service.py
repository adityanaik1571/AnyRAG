from services.embeddings.factory import EmbeddingFactory
from services.reasoning.prompt_builder import PromptBuilder
from services.vectorstores.factory import VectorStoreFactory
from core.logger import get_logger
from services.reasoning.interpreter.factory import InstructionInterpreterFactory
from services.llm.factory import LLMFactory

logger = get_logger(__name__)

class QueryService:
    def __init__(self):
        self.embedding_provider = EmbeddingFactory.create()
        self.embedding_model = self.embedding_provider.get_embedding_model()
        self.vector_store = VectorStoreFactory.create(embedding_model=self.embedding_model)
        self.llm_provider = LLMFactory.create()
        self.instruction_interpreter = InstructionInterpreterFactory.create(self.llm_provider)
    def ask(self, user_input: str) -> str:
        logger.info(f"Received query: {user_input}")
        logger.info("Retrieving relevant documents...")
        instruction = self.instruction_interpreter.interpret(user_input)
        documents = self.vector_store.retrieve(instruction.objective)
        logger.info(f"Retrieved {len(documents)} relevant documents.")
        prompt = PromptBuilder.build(instruction, documents)
        logger.info("Generating final response...")
        answer = self.llm_provider.invoke(prompt)
        return answer