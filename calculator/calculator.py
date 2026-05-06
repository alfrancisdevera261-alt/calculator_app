from operations.operation import (
    Addition, Subtraction, Multiplication,
    Division, Modulo, Exponentiation
)

from operations.exceptions import (
    InvalidOperationError,
    InvalidNumberError,
    DivisionByZeroError,
    CalculatorError
)

from calculator.validators import parse_number, validate_nonzero

from calculator.history import HistoryEntry

class Calculator:
    """
    Main Calculator Class
    
    Manages the calculator application including:
    - User menu and input handling
    - Operation selection (Add, Subtract, Multiply, etc.)
    - Input validation and error handling
    - Calculation history tracking
    
    Features:
    - Interactive menu-driven interface
    - Supports 6 operations: +, -, ×, ÷, %, ^
    - Custom exception handling for invalid inputs
    - Stores all calculations in history
    """