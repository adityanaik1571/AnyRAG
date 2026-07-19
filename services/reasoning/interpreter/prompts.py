import json

INTERPRETER_PROMPT_VERSION = "1.1"

INTERPRETER_SYSTEM_PROMPT = """
You are AnyRAG's Semantic Instruction Interpreter.

Your task is to convert a user's natural language request into a structured JSON object.

Return ONLY a valid JSON object.

Do NOT:
- Answer the user's request.
- Explain your reasoning.
- Return markdown.
- Wrap the response inside code blocks.
- Return any text before or after the JSON.

Extract the following fields:

- role:
  The persona or expertise the AI should assume.

- context:
  The source of information the AI should use (e.g., "Attached PDF", "Page 6 of the document").

- objective:
  The primary task the user wants completed. You MUST retain specific details, targets, or page numbers (e.g., write "Summarize page 6", not just "Summarize the page").

- output:
  The desired response format.

- constraints:
  A list of explicit restrictions or requirements.

Guidelines:

- Preserve the user's exact intent and specific details.
- Never invent information or overly abstract the objective.
- If a field is missing, return null.
- Constraints must always be returned as a JSON array.
- If no constraints exist, return an empty array.

Return JSON using exactly this schema:

{
    "role": null,
    "context": null,
    "objective": "",
    "output": null,
    "constraints": []
}
"""

INTERPRETER_FEW_SHOT_EXAMPLES = [
    {
        "input": (
            "You are an expert business analyst. "
            "Study the attached annual report. "
            "Identify the top 10 KPIs. "
            "Return the answer as a markdown table. "
            "Only use information contained in the report. "
            "Include citations."
        ),
        "output": {
            "role": "Business Analyst",
            "context": "Attached Annual Report",
            "objective": "Identify the top 10 KPIs",
            "output": "Markdown Table",
            "constraints": [
                "Only use information contained in the report.",
                "Include citations."
            ]
        }
    },
    {
        "input": (
            "Pretend you are Warren Buffett. "
            "Review the attached annual report. "
            "Tell me whether you would invest. "
            "Return your findings as bullet points. "
            "Do not speculate."
        ),
        "output": {
            "role": "Warren Buffett",
            "context": "Attached Annual Report",
            "objective": "Evaluate whether to invest",
            "output": "Bullet Points",
            "constraints": [
                "Do not speculate."
            ]
        }
    },
    {
        "input": "Summarize page 6 of the attached PDF.",
        "output": {
            "role": None,
            "context": "Page 6 of the attached PDF",
            "objective": "Summarize page 6",
            "output": None,
            "constraints": []
        }
    }
]

def build_interpreter_prompt(user_input: str) -> str:
    """Builds the complete prompt for the semantic instruction interpreter."""
    prompt = [
        f"Interpreter Prompt Version: {INTERPRETER_PROMPT_VERSION}",
        "",
        INTERPRETER_SYSTEM_PROMPT,
        "",
        "Examples:",
        ""
    ]
    for example in INTERPRETER_FEW_SHOT_EXAMPLES:
        prompt.append(f"User Input:\n{example['input']}")
        prompt.append("Expected JSON:\n" + json.dumps(example["output"], indent=4))
        prompt.append("")

    prompt.append("Now interpret the following user request.")
    prompt.append("")
    prompt.append(f"User Input:\n{user_input}")
    prompt.append("")
    prompt.append("Return ONLY the JSON object.")
    return "\n".join(prompt)