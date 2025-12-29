from pydantic import BaseModel

class transaction(BaseModel):
    step: int
    types: int
    amount: float