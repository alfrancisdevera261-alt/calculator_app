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

