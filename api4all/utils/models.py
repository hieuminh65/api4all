from dataclasses import dataclass

@dataclass
class TextResponse:
    content: str
    cost: float
    execution_time: float
    actual_time: float
    input_tokens: int
    output_tokens: int
    provider: str