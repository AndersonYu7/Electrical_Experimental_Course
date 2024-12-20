from class4_import_practice import square_root

def main():
    """Test the square_root function with a sample input."""
    number = float(input("Enter a number to find its square root: "))
    
    try:
        result = square_root(number)
        print(f"The square root of {number} is {result}.")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
