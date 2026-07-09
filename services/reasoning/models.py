from pydantic import BaseModel, Field

class ParsedInstruction(BaseModel):
    role: str | None = None
    context: str | None = None
    objective: str
    output: str | None = None
    constraints: list[str] = Field(default_factory=list)

class UserInstruction(BaseModel):
    user_input: str
    role: str | None = None
    context: str | None = None
    objective: str
    output: str | None = None
    constraints: list[str] = Field(default_factory=list)