def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats to handle division
        numerator = float(numerator)
        denominator = float(denominator)

        # Attempt division
        result = numerator / denominator
    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")
        return None
    except ValueError:
        # Handle invalid input types (e.g., if non-numeric values are passed)
        print("Error: Please enter numeric values only.")
        return None
    else:
        # No errors, return the result
        return result
    finally:
        # Optional: This block always runs, regardless of whether an exception occurred or not
        print("Division operation complete.")
