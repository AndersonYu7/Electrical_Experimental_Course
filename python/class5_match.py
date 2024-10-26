def calculator(num1, num2=None, operator=''):
    """
    Performs arithmetic operations based on the given operator.
    
    Supported operators:
    +, -, *, /, %, //, **2 (square), **10 (power of 10)
    """
    if operator in {'/', '//'} and num2 == 0:
        return "Error: Division by zero"

    # Dictionary-based dispatch to map operators to operations
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '%': lambda a, b: a % b,
        '//': lambda a, b: a // b,
        '**2': lambda a, _: f"{a} ** 2 = {a ** 2}",
        '**10': lambda a, _: f"{a} ** 10 = {a ** 10}",
    }

    # Validate the operator
    if operator not in operations:
        return f"Error: Invalid operator (Operation: {num1} {operator} {num2})"

    # Perform the operation
    result = operations[operator](num1, num2)
    
    # For regular operations, format the result nicely
    if isinstance(result, (int, float)):
        return f"{num1} {operator} {num2} = {result}"
    return result

if __name__ == "__main__":
    # Test cases
    print(calculator(10, 5, '+'))    # 10 + 5 = 15
    print(calculator(10, 5, '-'))    # 10 - 5 = 5
    print(calculator(10, 5, '*'))    # 10 * 5 = 50
    print(calculator(10, 5, '/'))    # 10 / 5 = 2.0
    print(calculator(10, 5, '%'))    # 10 % 5 = 0
    print(calculator(10, 5, '//'))   # 10 // 5 = 2
    print(calculator(3, operator='**2'))   # 3 ** 2 = 9
    print(calculator(2, operator='**10'))  # 2 ** 10 = 1024
    print(calculator(10, 5, '^'))    # Error: Invalid operator
