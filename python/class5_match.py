def calculator(num1, num2, operator):
    """Performs arithmetic operations based on the given operator."""
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operator == '%':
        result = num1 % num2
    elif operator == '//':
        if num2 != 0:
            result = num1 // num2
        else:
            return "Error: Division by zero"
    elif operator == '**2':
        result = num1 ** 2
        return f"{num1} ** 2 = {result}"
    elif operator == '**10':
        result = num1 ** 10
        return f"{num1} ** 10 = {result}"
    else:
        return f"Error: Invalid operator (Operation: {num1} {operator} {num2})"

    return f"{num1} {operator} {num2} = {result}"

if __name__ == "__main__":
    # Test cases
    print(calculator(10, 5, '+'))    # 10 + 5 = 15
    print(calculator(10, 5, '-'))    # 10 - 5 = 5
    print(calculator(10, 5, '*'))    # 10 * 5 = 50
    print(calculator(10, 5, '/'))    # 10 / 5 = 2.0
    print(calculator(10, 5, '%'))    # 10 % 5 = 0
    print(calculator(10, 5, '//'))   # 10 // 5 = 2
    print(calculator(3, None, '**2'))   # 3 ** 2 = 9
    print(calculator(2, None, '**10'))  # 2 ** 10 = 1024
    print(calculator(10, 5, '^'))    # Error: Invalid operator
