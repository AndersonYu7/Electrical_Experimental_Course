def read_and_process_file(filename, power=2):
    """Reads a file, checks for numeric content, and performs power operations."""
    try:
        # Attempt to open the file
        file = open(filename, 'r')

        # Read content and strip any surrounding whitespace
        content = file.read().strip()

        # Check if the content is numeric
        if not content.isdigit():
            raise ValueError("File content must be a pure number.")

        # Convert content to an integer for processing
        number = int(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        # Perform power operation and print the result
        result = number ** power
        print(f"The number {number} raised to the power of {power} is {result}.")
    finally:
        # Ensure the file is closed properly
        try:
            file.close()
        except NameError:
            # If the file was never opened, ignore this exception
            pass

# Example usage:
if __name__ == "__main__":
    filename = input("Enter the filename: ")
    read_and_process_file(filename, power=3)
