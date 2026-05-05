from datetime import datetime

class HistoryEntry:
    def __init__(self, expression, result):
        self.expression = expression
        self.result = result
        self.timestamp = datetime.now().strftime("%H:%M:%S")

    def __str__(self):
        return f"[{self.timestamp}] {self.expression} = {self.result}"