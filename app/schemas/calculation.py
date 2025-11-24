
from pydantic import BaseModel, field_validator
from typing import Optional

class CalculationCreate(BaseModel):
    a: float
    b: float
    type: str

    @field_validator("type")
    def validate_type(cls, v):
        allowed = {"Add", "Sub", "Multiply", "Divide"}
        if v not in allowed:
            raise ValueError("Invalid type. Must be Add, Sub, Multiply, Divide")
        return v

    @field_validator("b")
    def check_divisor(cls, v, values):
        if values.get("type") == "Divide" and v == 0:
            raise ValueError("Cannot divide by zero")
        return v


class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: str
    result: Optional[float]

    class Config:
        from_attributes = True

