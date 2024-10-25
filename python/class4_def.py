def factorial(n):
    """Recursively calculates the factorial of a given integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    try:
        number = int(input("Enter a positive integer: "))
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
    except ValueError as ve:
        print(f"Error: {ve}")
