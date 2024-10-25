import random

def generate_numbers():
    """Generate a list with four even numbers and one odd number."""
    numbers = [2, 4, 6, 8, 10]

    # Randomly select an index (not the last one) to make an odd number.
    odd_index = random.randint(0, len(numbers) - 2)
    numbers[odd_index] += 1  # Convert the even number to an odd number.
    
    return numbers

def find_first_odd(numbers):
    """Find and print the first odd number with its position."""
    for index, num in enumerate(numbers):
        if num % 2 != 0:  # Check if the number is odd.
            print(f"The {index + 1}th item is odd, and its value is {num}.")
            break  # Exit the loop after finding the first odd number.

def main():
    """Generate numbers and find the first odd number."""
    numbers = generate_numbers()
    print(f"The numbers list is: {numbers}")
    find_first_odd(numbers)

if __name__ == "__main__":
    main()
