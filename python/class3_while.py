import random

def generate_number():
    """Generate a 4-digit number with non-repeating digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]

def evaluate_guess(secret, guess):
    """
    Evaluate the user's guess.

    Args:
        secret (list): The generated 4-digit secret number.
        guess (list): The user's guessed 4-digit number.

    Returns:
        tuple: A (correct digit and position), B (correct digit, wrong position).
    """
    a = sum(s == g for s, g in zip(secret, guess))
    b = sum(g in secret for g in guess) - a
    return a, b

def main():
    """Play the 1A2B guessing game."""
    secret = generate_number()
    attempts = 0

    print("Welcome to the 1A2B guessing game!")
    print("Guess the 4-digit number with non-repeating digits.")

    while True:
        user_input = input("Enter your guess: ")

        # Validate input: must be 4 digits, non-repeating, and numeric
        if len(user_input) != 4 or not user_input.isdigit() or len(set(user_input)) != 4:
            print("Invalid input! Please enter 4 unique digits.")
            continue

        guess = [int(d) for d in user_input]
        attempts += 1

        a, b = evaluate_guess(secret, guess)
        print(f"{a}A{b}B")

        if a == 4:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
