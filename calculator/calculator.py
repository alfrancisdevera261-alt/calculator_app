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
    
    MENU = {
        "1": Addition(),
        "2": Subtraction(),
        "3": Multiplication(),
        "4": Division(),
        "5": Modulo(),
        "6": Exponentiation(),
    }

    def __init__(self):
        self.history = []

    def get_number(self, prompt):
        raw = input(prompt)
        try:
            return parse_number(raw)
        except ValueError:
            raise InvalidNumberError(raw)
        
    def get_operation(self, choice):
        if choice not in self.MENU:
            raise InvalidOperationError(choice)
        return self.MENU[choice]
    
    def run(self):
        while True:
            try:
                print("\n1:Add 2:Sub 3:Mul 4:Div 5:Mod 6:Exp Q:Quit")
                choice = input("Enter choice: ").upper()

                if choice == "Q":
                    break

                operation = self.get_operation(choice)
                
                a = self.get_number("A: ")
                b = self.get_number("B: ")
                
                try:
                    if isinstance(operation, (Division, Modulo)):
                        validate_nonzero(b)

                    result = operation.execute(a, b)

                except ZeroDivisionError:
                    raise DivisionByZeroError()