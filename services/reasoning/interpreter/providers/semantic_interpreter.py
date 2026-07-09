from services.reasoning.interpreter.base import BaseInstructionInterpreter
from services.reasoning.interpreter.prompts import build_interpreter_prompt
from services.reasoning.models import UserInstruction, ParsedInstruction
from core.logger import get_logger

logger = get_logger(__name__)

class SemanticInstructionInterpreter(BaseInstructionInterpreter):
    def __init__(self, llm):
        self.llm_provider = llm
    def interpret(self, user_input: str) -> UserInstruction:
        logger.info("Interpreting user instruction...")
        prompt = build_interpreter_prompt(user_input)
        response = self.llm_provider.invoke(prompt)
        parsed_response = ParsedInstruction.model_validate_json(response)
        instruction = UserInstruction(user_input=user_input,
                                      role=parsed_response.role,
                                      context=parsed_response.context,
                                      objective=parsed_response.objective,
                                      output=parsed_response.output,
                                      constraints=parsed_response.constraints)
        logger.info("Successfully interpreted user instruction.")
        return instruction