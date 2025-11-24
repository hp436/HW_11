import pytest
from app.schemas.calculation import CalculationCreate

def test_valid_schema():
    c = CalculationCreate(a=3, b=2, type="Add")
    assert c.type == "Add"

def test_zero_division():
    with pytest.raises(ValueError):
        CalculationCreate(a=3, b=0, type="Divide")

