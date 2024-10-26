import math

def calculator():
    """A complex calculator for division, square root, and modulo operations."""

    operations = {
        '/': lambda a, b: a / b if b != 0 else "Error: Division by zero.",
        '%': lambda a, b: a % b,
        'sqrt': lambda a, _: math.sqrt(a) if a >= 0 else "Error: Negative square root.",
    }

    try:
        # Get user input for the first number and operation
        num1 = float(input("Enter the first number: "))
        operation = input("Enter an operation ('/', 'sqrt', '%'): ").strip()

        # Get the second number if required
        num2 = None
        if operation in {'/', '%'}:
            num2 = float(input("Enter the second number: "))

        # Check if the operation is valid
        if operation not in operations:
            raise ValueError(f"Invalid operation: {operation}")

        # Perform the operation
        result = operations[operation](num1, num2)
        print(f"Result: {result}")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except TypeError:
        print("Error: Missing or incorrect operands.")
    else:
        print("Operation completed successfully.")
    finally:
        print("Calculator session ended.")

if __name__ == "__main__":
    calculator()
