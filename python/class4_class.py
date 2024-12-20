from calculatorAPI import CalculatorTwo

def main():
    """Test the methods of CalculatorTwo with sample input."""
    cal2 = CalculatorTwo()

    # Test cases for CalculatorTwo methods with detailed output
    result_add = cal2.add(1, 2, 3, 4)
    print(f"(1 + 2) + (3 + 4) = {result_add}")

    result_subtract = cal2.subtract(10, 5, 3, 1)
    print(f"(10 + 5) - (3 + 1) = {result_subtract}")

    result_multiply = cal2.multiply(2, 3, 4, 5)
    print(f"(2 * 3) * (4 * 5) = {result_multiply}")

    result_divide = cal2.divide(8, 2, 12, 3)
    print(f"(8 / 2) / (12 / 3) = {result_divide}")

if __name__ == "__main__":
    main()
