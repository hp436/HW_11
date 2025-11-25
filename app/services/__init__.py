
"""Services Module"""
from app.services.factory import (
    CalculationFactory,
    CalculationStrategy,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    perform_calculation
)

__all__ = [
    "CalculationFactory",
    "CalculationStrategy",
    "AddCalculation",
    "SubtractCalculation",
    "MultiplyCalculation",
    "DivideCalculation",
    "perform_calculation"
]
```

---

## 🎯 **What to Update on GitHub**

1. **Edit** `tests/test_factory.py`
   - Change import from `app.factory.calculation_factory` to `app.services.factory`
   - Use the complete code above

2. **Verify** `app/services/factory.py` has all the factory code

3. **Update** `app/services/__init__.py` with exports

4. **Commit** and push

---

## ✅ **Expected Result**

After fixing the import:
```
Run pytest -v --timeout=10
============================= test session starts ==============================
collected 12 items

tests/test_factory.py::test_add PASSED                               [  8%]
tests/test_factory.py::test_subtract PASSED                          [ 16%]
tests/test_factory.py::test_multiply PASSED                          [ 25%]
tests/test_factory.py::test_divide PASSED                            [ 33%]
tests/test_factory.py::test_invalid PASSED                           [ 41%]
tests/test_factory.py::test_divide_by_zero PASSED                    [ 50%]
tests/test_factory.py::test_factory_creates_add PASSED               [ 58%]
tests/test_factory.py::test_factory_creates_subtract PASSED          [ 66%]
tests/test_factory.py::test_factory_creates_multiply PASSED          [ 75%]
tests/test_factory.py::test_factory_creates_divide PASSED            [ 83%]
tests/test_factory.py::test_get_supported_types PASSED               [ 91%]
tests/test_factory.py::test_negative_numbers PASSED                  [100%]

==================== 12 passed in 1.23s ====================
