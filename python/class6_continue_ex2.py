def print_even_numbers():
    """Print even numbers from 0 to 100, 10 numbers per line."""
    count = 0  # Track how many numbers have been printed on the current line

    for i in range(101):
        if i % 2 != 0:
            continue
        print(f"{i:2}", end=' ')  # Print with fixed-width alignment
        count += 1

        if count % 10 == 0:  # Start a new line every 10 numbers
            print()

if __name__ == "__main__":
    print_even_numbers()
