from app.services.factory import OperationFactory

def test_add():
    op = OperationFactory.get_operation("Add")
    assert op.compute(3, 2) == 5

def test_invalid():
    try:
        OperationFactory.get_operation("Bad")
        assert False
    except ValueError:
        assert True

