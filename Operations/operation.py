from abc import ABC, abstractmethod

from operations.exceptions import DivisionByZeroError

class Operation(ABC):
    """
    Abstract class: cannot be instantiated directly
    All child classes must implement execute()
    """
    symbol = ""
    name = ""

    @abstractmethod
    def execute(self, a, b):
        pass  
    
    def describe(self, a, b, result):
        return f"{a} {self.symbol} {b} = {result}"
    
    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Addition(Operation):
    symbol = "+"
    name = "Addition"

    def execute(self, a, b):
        return a + b


class Subtraction(Operation):
    symbol = "-"
    name = "Subtraction"

    def execute(self, a, b):
        return a - b


class Multiplication(Operation):
    symbol = "×"
    name = "Multiplication"

    def execute(self, a, b):
        return a * b


class Division(Operation):
    symbol = "÷"
    name = "Division"

    def execute(self, a, b):
        if b == 0:
            raise DivisionByZeroError()
        return a / b


class Modulo(Operation):
    symbol = "%"
    name = "Modulo"

    def execute(self, a, b):
        if b == 0:
            raise DivisionByZeroError()
        return a % b


class Exponentiation(Operation):
    symbol = "^"
    name = "Exponentiation"

    def execute(self, a, b):
        return a ** b