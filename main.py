import black

def format_code(file_path):
    # Load the contents of the file
    with open(file_path, "r") as file:
        code = file.read()

    # Format the code using Black
    formatted_code = black.format_file_contents(
        code,
        fast=True,  # Use the fast mode for quicker formatting
        mode=black.FileMode(),  # Use the default file mode
    )

    # Write the formatted code back to the file
    with open(file_path, "w") as file:
        file.write(formatted_code)


# Usage example
if __name__ == "__main__":
    # Specify the path to the Python file you want to format
    python_file_path = "path/to/your/file.py"

    # Format the code
    format_code(python_file_path)
