class BaseOperation:
    def compute(self, a, b):
        raise NotImplementedError


class AddOperation(BaseOperation):
    def compute(self, a, b):
        return a + b


class SubOperation(BaseOperation):
    def compute(self, a, b):
        return a - b


class MultiplyOperation(BaseOperation):
    def compute(self, a, b):
        return a * b


class DivideOperation(BaseOperation):
    def compute(self, a, b):
        return a / b


class OperationFactory:
    @staticmethod
    def get_operation(operation_type: str):
        ops = {
            "Add": AddOperation(),
            "Sub": SubOperation(),
            "Multiply": MultiplyOperation(),
            "Divide": DivideOperation(),
        }
        if operation_type not in ops:
            raise ValueError("Invalid operation type")
        return ops[operation_type]

