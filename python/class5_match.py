def calculator(num1, num2=None, operator=''):
    """
    Performs arithmetic operations based on the given operator.
    
    Supported operators:
    +, -, *, /, %, //, **2 (square), **10 (power of 10)
    """

    try:
        # Dictionary-based dispatch with lambda functions
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else "Error: Division by zero",
            '%': lambda a, b: a % b,
            '//': lambda a, b: a // b if b != 0 else "Error: Division by zero",
            '**2': lambda a, _: f"{a} ** 2 = {a ** 2}",
            '**10': lambda a, _: f"{a} ** 10 = {a ** 10}"
        }

        # Check if the operator is valid
        if operator not in operations:
            raise ValueError(f"Invalid operator: {operator}")

        # Handle operations with a single operand (like **2, **10)
        if operator in {'**2', '**10'}:
            return operations[operator](num1, None)

        # Ensure both operands are provided for binary operations
        if num2 is None:
            raise ValueError(f"Operator {operator} requires two operands.")

        # Perform the operation and return the result
        result = operations[operator](num1, num2)

        # Format the result for binary operations
        if isinstance(result, (int, float)):
            return f"{num1} {operator} {num2} = {result}"
        return result

    except ValueError as ve:
        return f"Error: {ve}"
    except TypeError:
        return "Error: Invalid input type. Please enter numbers only."

if __name__ == "__main__":
    # Test cases
    print(calculator(10, 5, '+'))    # 10 + 5 = 15
    print(calculator(10, 5, '-'))    # 10 - 5 = 5
    print(calculator(10, 5, '*'))    # 10 * 5 = 50
    print(calculator(10, 0, '/'))    # Error: Division by zero
    print(calculator(10, 5, '%'))    # 10 % 5 = 0
    print(calculator(10, 5, '//'))   # 10 // 5 = 2
    print(calculator(3, operator='**2'))  # 3 ** 2 = 9
    print(calculator(2, operator='**10')) # 2 ** 10 = 1024
    print(calculator(10, 5, '^'))    # Error: Invalid operator: ^
    print(calculator(10, None, '+')) # Error: Operator + requires two operands.
    print(calculator('10', 5, '+'))  # Error: Invalid input type.
