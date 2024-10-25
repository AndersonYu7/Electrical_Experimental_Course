class CalculatorOne:
    """A class with basic arithmetic operations for two numbers."""

    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def subtract(self, a, b):
        """Subtract the second number from the first and return the result."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b

    def divide(self, a, b):
        """Divide the first number by the second and return the result."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

class CalculatorTwo(CalculatorOne):
    """
    A class that extends CalculatorOne to perform arithmetic on four numbers
    by using the parent class methods with the `super()` function.
    """

    def add(self, a, b, c, d):
        """Add four numbers using the parent class add method."""
        return super().add(a, b) + super().add(c, d)

    def subtract(self, a, b, c, d):
        """Subtract the sum of c and d from the sum of a and b."""
        return super().subtract(super().add(a, b), super().add(c, d))

    def multiply(self, a, b, c, d):
        """Multiply two pairs of numbers and return the product."""
        return super().multiply(a, b) * super().multiply(c, d)

    def divide(self, a, b, c, d):
        """Divide the result of two divisions."""
        return super().divide(a, b) / super().divide(c, d)
