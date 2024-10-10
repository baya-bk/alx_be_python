def safe_divide(numerator, denominator):
    try:
        # Attempt division
        result = numerator / denominator
    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        # Handle invalid input types (e.g., if non-numeric values are passed)
        print("Error: Both inputs must be numbers.")
        return None
    else:
        # No errors, return the result
        return result
    finally:
        # Optional: This block always runs, regardless of whether an exception occurred or not
        print("Division operation complete.")
