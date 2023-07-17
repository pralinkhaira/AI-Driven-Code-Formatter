# AI-Driven Code Formatter

The AI-Driven Code Formatter is a tool that utilizes artificial intelligence and machine learning techniques to automatically format and optimize code written in various programming languages. It aims to improve code readability, maintainability, and adherence to coding style guidelines without requiring manual intervention from developers.

## Installation

1. Install the Black library by running the following command:
   ```shell
   pip install black
   ```

## Usage

To use the AI-Driven Code Formatter, follow these steps:

1. Open the Python file you want to format.

2. Import the Black library in your Python script:
   ```python
   import black
   ```

3. Define the `format_code` function that takes a file path as input, formats the code using Black, and writes the formatted code back to the file. Here's an example:
   ```python
   def format_code(file_path):
       with open(file_path, "r") as file:
           code = file.read()

       formatted_code = black.format_file_contents(
           code,
           fast=True,
           mode=black.FileMode(),
       )

       with open(file_path, "w") as file:
           file.write(formatted_code)
   ```

4. In the `main` block, specify the path to the Python file you want to format:
   ```python
   if __name__ == "__main__":
       python_file_path = "path/to/your/file.py"
       format_code(python_file_path)
   ```

5. Save the script, and then run it. It will format the specified Python file using Black's formatting rules.

Feel free to customize the code according to your specific needs and project requirements.

## Update History

### Update V1.1 - 17-07-2023: 

- Added error handling for cases where the code is already well-formatted using black.NothingChanged exception.
- Implemented command-line argument parsing using argparse module for better user interaction.
- Introduced a separate main function to encapsulate the main execution logic, improving code organization and reusability.

## Contributing

Contributions to the AI-Driven Code Formatter project are welcome! If you would like to contribute, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
