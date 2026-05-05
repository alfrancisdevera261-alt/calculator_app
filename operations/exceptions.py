class CalculatorError(Exception):
    """Base class for all calculator-related errors"""
    pass

class InvalidOperationError(CalculatorError):
    """Raised when user selects invalid menu option"""
    def __init__(self, choice):
        super().__init__(f"'{choice}' is not a valid operation.")