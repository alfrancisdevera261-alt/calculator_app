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
        pass  # forces child classes to implement this
