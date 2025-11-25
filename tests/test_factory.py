"""
Complete Factory Tests - With Timeouts to Prevent Hanging
"""
import pytest
from app.factory.calculation_factory import (
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    perform_calculation
)


@pytest.mark.timeout(5)
def test_add():
    """Test addition through factory"""
    result = perform_calculation(10, 5, "Add")
    assert result == 15
    
    result2 = perform_calculation(-5, 3, "Add")
    assert result2 == -2


@pytest.mark.timeout(5)
def test_subtract():
    """Test subtraction through factory"""
    result = perform_calculation(10, 5, "Subtract")
    assert result == 5
    
    result2 = perform_calculation(3, 5, "Subtract")
    assert result2 == -2


@pytest.mark.timeout(5)
def test_multiply():
    """Test multiplication through factory"""
    result = perform_calculation(10, 5, "Multiply")
    assert result == 50
    
    result2 = perform_calculation(-5, 3, "Multiply")
    assert result2 == -15


@pytest.mark.timeout(5)
def test_divide():
    """Test division through factory"""
    result = perform_calculation(10, 5, "Divide")
    assert result == 2
    
    result2 = perform_calculation(6, 3, "Divide")
    assert result2 == 2


@pytest.mark.timeout(5)
def test_invalid():
    """Test invalid calculation type"""
    with pytest.raises(ValueError, match="Invalid calculation type"):
        CalculationFactory.create_calculation("Invalid")


@pytest.mark.timeout(5)
def test_divide_by_zero():
    """Test division by zero raises error"""
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        perform_calculation(10, 0, "Divide")


@pytest.mark.timeout(5)
def test_factory_creates_strategies():
    """Test that factory creates correct strategy instances"""
    add_calc = CalculationFactory.create_calculation("Add")
    assert isinstance(add_calc, AddCalculation)
    assert add_calc.calculate(5, 3) == 8
    
    sub_calc = CalculationFactory.create_calculation("Subtract")
    assert isinstance(sub_calc, SubtractCalculation)
    assert sub_calc.calculate(5, 3) == 2
    
    mul_calc = CalculationFactory.create_calculation("Multiply")
    assert isinstance(mul_calc, MultiplyCalculation)
    assert mul_calc.calculate(5, 3) == 15
    
    div_calc = CalculationFactory.create_calculation("Divide")
    assert isinstance(div_calc, DivideCalculation)
    assert div_calc.calculate(6, 3) == 2


@pytest.mark.timeout(5)
def test_get_supported_types():
    """Test getting list of supported calculation types"""
    types = CalculationFactory.get_supported_types()
    assert "Add" in types
    assert "Subtract" in types
    assert "Multiply" in types
    assert "Divide" in types
    assert len(types) == 4


@pytest.mark.timeout(5)
def test_calculation_with_floats():
    """Test calculations with decimal numbers"""
    result = perform_calculation(10.5, 2.5, "Add")
    assert result == 13.0
    
    result2 = perform_calculation(10.0, 3.0, "Divide")
    assert abs(result2 - 3.333333) < 0.001


@pytest.mark.timeout(5)
def test_calculation_with_negatives():
    """Test calculations with negative numbers"""
    assert perform_calculation(-10, -5, "Add") == -15
    assert perform_calculation(-10, -5, "Subtract") == -5
    assert perform_calculation(-10, -5, "Multiply") == 50
    assert perform_calculation(-10, -5, "Divide") == 2


@pytest.mark.timeout(5)
def test_calculation_with_zero():
    """Test calculations with zero"""
    assert perform_calculation(10, 0, "Add") == 10
    assert perform_calculation(10, 0, "Subtract") == 10
    assert perform_calculation(10, 0, "Multiply") == 0
    assert perform_calculation(0, 5, "Add") == 5


@pytest.mark.timeout(5)
def test_large_numbers():
    """Test calculations with large numbers"""
    result = perform_calculation(1000000, 2000000, "Add")
    assert result == 3000000
    
    result2 = perform_calculation(1e10, 2e10, "Add")
    assert result2 == 3e10
