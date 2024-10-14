def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats to handle division
        numerator = float(numerator)
        denominator = float(denominator)

        # Attempt division
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    except ValueError:
        # Handle invalid input types (e.g., if non-numeric values are passed)
        return "Error: Please enter numeric values only."
