import random

def generate_numbers():
    """Generate a list with four even numbers and one odd number."""
    numbers = [2, 4, 6, 8, 10]

    # Randomly select an index (not the last one) to make an odd number.
    odd_index = random.randint(0, len(numbers) - 2)
    numbers[odd_index] += 1  # Convert the selected even number to an odd number.
    
    return numbers

def print_even_numbers(numbers):
    """Traverse the list and print even numbers using a while loop."""
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 != 0:  # Skip if the number is odd.
            i += 1
            continue
        # Print the even number with its position.
        print(f"The {i + 1}th item is even, and its value is {numbers[i]}")
        i += 1

def main():
    """Generate numbers and print all even numbers."""
    numbers = generate_numbers()
    print(f"The numbers list is: {numbers}")
    print_even_numbers(numbers)

if __name__ == "__main__":
    main()
