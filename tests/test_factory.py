"""
Factory Tests - Fixed for your structure
"""
import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.factory import (
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    perform_calculation
)


@pytest.mark.timeout(5)
def test_add():
    """Test addition"""
    result = perform_calculation(10, 5, "Add")
    assert result == 15


@pytest.mark.timeout(5)
def test_subtract():
    """Test subtraction"""
    result = perform_calculation(10, 5, "Subtract")
    assert result == 5


@pytest.mark.timeout(5)
def test_multiply():
    """Test multiplication"""
    result = perform_calculation(10, 5, "Multiply")
    assert result == 50


@pytest.mark.timeout(5)
def test_divide():
    """Test division"""
    result = perform_calculation(10, 5, "Divide")
    assert result == 2


@pytest.mark.timeout(5)
def test_invalid():
    """Test invalid calculation type"""
    with pytest.raises(ValueError, match="Invalid calculation type"):
        CalculationFactory.create_calculation("Invalid")


@pytest.mark.timeout(5)
def test_divide_by_zero():
    """Test division by zero"""
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        perform_calculation(10, 0, "Divide")


@pytest.mark.timeout(5)
def test_factory_creates_add():
    """Test factory creates Add strategy"""
    calc = CalculationFactory.create_calculation("Add")
    assert isinstance(calc, AddCalculation)
    assert calc.calculate(5, 3) == 8


@pytest.mark.timeout(5)
def test_factory_creates_subtract():
    """Test factory creates Subtract strategy"""
    calc = CalculationFactory.create_calculation("Subtract")
    assert isinstance(calc, SubtractCalculation)
    assert calc.calculate(5, 3) == 2


@pytest.mark.timeout(5)
def test_factory_creates_multiply():
    """Test factory creates Multiply strategy"""
    calc = CalculationFactory.create_calculation("Multiply")
    assert isinstance(calc, MultiplyCalculation)
    assert calc.calculate(5, 3) == 15


@pytest.mark.timeout(5)
def test_factory_creates_divide():
    """Test factory creates Divide strategy"""
    calc = CalculationFactory.create_calculation("Divide")
    assert isinstance(calc, DivideCalculation)
    assert calc.calculate(6, 3) == 2


@pytest.mark.timeout(5)
def test_get_supported_types():
    """Test getting supported types"""
    types = CalculationFactory.get_supported_types()
    assert "Add" in types
    assert "Subtract" in types
    assert "Multiply" in types
    assert "Divide" in types
    assert len(types) == 4


@pytest.mark.timeout(5)
def test_negative_numbers():
    """Test with negative numbers"""
    assert perform_calculation(-10, -5, "Add") == -15
    assert perform_calculation(-10, -5, "Subtract") == -5
    assert perform_calculation(-10, -5, "Multiply") == 50
    assert perform_calculation(-10, -5, "Divide") == 2
