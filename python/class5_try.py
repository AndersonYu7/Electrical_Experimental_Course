import math

def calculator():
    """A complex calculator for division, square root, and modulo operations."""
    try:
        # User input for the first number and the operation
        num1 = float(input("Enter the first number: "))
        operation = input(
            "Enter an operation (/ for division, sqrt for square root, % for modulo): "
        )

        # If operation is division or modulo, request a second number
        if operation in ('/', '%'):
            num2 = float(input("Enter the second number: "))

        # Perform the selected operation
        if operation == '/':
            result = num1 / num2
        elif operation == 'sqrt':
            if num1 < 0:
                raise ValueError("Cannot calculate square root of a negative number!")
            result = math.sqrt(num1)
        elif operation == '%':
            result = num1 % num2
        else:
            print("Invalid operation")
            return

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Result: {result}")
    finally:
        print("Operation completed")


if __name__ == "__main__":
    calculator()
