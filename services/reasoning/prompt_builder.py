from langchain_core.documents import Document
from core.logger import get_logger
from services.reasoning.models import UserInstruction

logger = get_logger(__name__)

ANSWER_SYSTEM_PROMPT = """
You are a helpful AI assistant.

Use ONLY the retrieved context to answer the user's request.

If the answer cannot be found in the context,
say you do not know.

Never hallucinate.
"""

ROLE_HEADER = "Role"
CONTEXT_HEADER = "Retrieved Context"
OBJECTIVE_HEADER = "Objective"
OUTPUT_HEADER = "Output Format"
CONSTRAINT_HEADER = "Constraints"
ANSWER_HEADER = "Answer"

class PromptBuilder:
    """Builds the final prompt sent to the answering LLM."""
    @staticmethod
    def build(instruction: UserInstruction, documents: list[Document]) -> str:
        logger.info("Building answer prompt...")
        prompt = []
        if instruction.role:
            prompt.append(f"{ROLE_HEADER}:\n{instruction.role}\n")
        prompt.append(ANSWER_SYSTEM_PROMPT)
        prompt.append("")
        prompt.append(f"{CONTEXT_HEADER}:\n")

        for index, document in enumerate(documents, start=1):
            prompt.append(f"[Document {index}]")
            prompt.append(document.page_content)
            prompt.append("")

        prompt.append(f"{OBJECTIVE_HEADER}:")
        prompt.append(instruction.objective)
        prompt.append("")

        if instruction.output:
            prompt.append(f"{OUTPUT_HEADER}:")
            prompt.append(instruction.output)
            prompt.append("")

        if instruction.constraints:
            prompt.append(f"{CONSTRAINT_HEADER}:")
            for constraint in instruction.constraints:
                prompt.append(f"- {constraint}")
            prompt.append("")

        prompt.append(f"{ANSWER_HEADER}:")
        prompt.append(
            """Answer the user's request using only the retrieved context above.

If the answer cannot be found in the retrieved context, explicitly state that you do not know.

Do not fabricate or infer information that is not present."""
        )
        logger.info("Answer prompt built successfully.")
        return "\n".join(prompt)

# TODO:
# Refactor PromptBuilder into smaller helper methods
# when additional prompt sections (chat history, citations,
# images, tool outputs, etc.) are introduced.