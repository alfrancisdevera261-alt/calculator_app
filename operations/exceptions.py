class CalculatorError(Exception):
    """Base class for all calculator-related errors"""
    pass

class InvalidOperationError(CalculatorError):
    """Raised when user selects invalid menu option"""
    def __init__(self, choice):
        super().__init__(f"'{choice}' is not a valid operation.")
        
class DivisionByZeroError(CalculatorError):
    """Raised when dividing by zero"""
    def __init__(self):
        super().__init__("Cannot divide by zero.")
        
class InvalidNumberError(CalculatorError):
    """Raised when input is not a number"""
    def __init__(self, value):
        super().__init__(f"'{value}' is not a valid number.")