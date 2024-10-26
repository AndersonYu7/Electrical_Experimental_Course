import math

def calculator():
    """A complex calculator for division, square root, and modulo operations."""

    try:
        # User input for the first number and operation
        num1 = float(input("Enter the first number: "))
        operation = input("Enter an operation ('/' for division, 'sqrt' for square root, '%' for modulo): ").strip()

        # Define operations using lambda functions
        operations = {
            '/': lambda a, b: a / b,  #raise ZeroDivisionError
            '%': lambda a, b: a % b,
            'sqrt': lambda a: math.sqrt(a) if a >= 0 else raise_negative_sqrt_error()
        }

        # If the operation requires a second number, get num2
        num2 = None
        if operation in {'/', '%'}:
            num2 = float(input("Enter the second number: "))

        # Check if the operation is valid
        if operation not in operations:
            raise ValueError(f"Invalid operation: {operation}")

        # Execute the operation
        if operation == 'sqrt':
            result = operations[operation](num1)
        else:
            result = operations[operation](num1, num2)

    # Handle invalid input (non-numeric or invalid operations)
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    # Handle division by zero
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    # Handle any other exceptions
    else:
        print(f"Result: {result}")
    finally:
        print("Operation completed.")

def raise_negative_sqrt_error():
    """Raise a ValueError for negative square root."""
    raise ValueError("Cannot calculate square root of a negative number!")

if __name__ == "__main__":
    calculator()
