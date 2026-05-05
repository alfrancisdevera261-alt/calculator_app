def parse_number(value):
    """
    Converts string to float
    Raises error if invalid
    """
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"'{value}' is not a valid number.")
    
def validate_nonzero(value):
    if value == 0:
        raise ZeroDivisionError("Cannot divide by zero.")