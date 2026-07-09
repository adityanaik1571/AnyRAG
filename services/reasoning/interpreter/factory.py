from config.settings import settings
from core.enums import InstructionInterpreterProvider, LLMProvider
from services.reasoning.interpreter.providers.semantic_interpreter import SemanticInstructionInterpreter
from services.llm.factory import LLMFactory
from core.logger import get_logger

INTERPRETER_REGISTRY = {
    InstructionInterpreterProvider.SEMANTIC: SemanticInstructionInterpreter,
}

logger = get_logger(__name__)

class InstructionInterpreterFactory:
    @staticmethod
    def create(llm_provider=None):
        logger.info(f"Creating Instruction Interpreter: {settings.instruction_interpreter_provider.value}")
        interpreter_class = INTERPRETER_REGISTRY.get(settings.instruction_interpreter_provider)
        if interpreter_class is None:
            raise NotImplementedError(f"Instruction interpreter {interpreter_class} is not implemented yet")
        if llm_provider is None:
            llm_provider = LLMFactory.create()
        return interpreter_class(llm_provider)

