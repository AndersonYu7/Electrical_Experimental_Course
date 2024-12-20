def is_valid_triangle(a, b, c):
    """Check if the given sides can form a valid triangle."""
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    """Determine the type of the triangle."""
    if not is_valid_triangle(a, b, c):
        return "These sides do not form a valid triangle."
    
    if a == b == c:
        return "This is an equilateral triangle."
    elif a == b or a == c or b == c:
        return "This is an isosceles triangle."
    else:
        return "This is a scalene triangle."

def main():
    """Take user input for three sides and determine the triangle type."""
    try:
        a = float(input("Enter the length of the first side: "))
        b = float(input("Enter the length of the second side: "))
        c = float(input("Enter the length of the third side: "))

        result = triangle_type(a, b, c)
        print(result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
