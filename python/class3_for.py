def multiplication_table():
    """Print the 9x9 multiplication table."""
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j:2}", end="  ")
        print()  # Newline after each row

if __name__ == "__main__":
    multiplication_table()
