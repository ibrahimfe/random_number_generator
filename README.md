# Random Password Generator

This is a Python script that generates a random password with customizable options.

## Usage

To use the `password_generator.py` script, run it with the desired arguments. The script takes the following arguments:

-   `length` (optional): The length of the password (default is 8).
-   `-p`, `--punctuation` (optional): Whether to include punctuation characters in the password.
-   `-n`, `--number` (optional): Whether to include numeric characters in the password.

Here's an example of how to use the script:

    $ python password_generator.py 12 --punctuation --number

This will generate a random password with a length of 12 characters that includes both punctuation and numbers.

## How it works

The `password_generator.py` script works by first defining sets of characters for each type of character that can be included in the password (lowercase letters, uppercase letters, digits, and punctuation). It then selects characters from these sets based on the desired options, and uses the `random.choice()` function to select a random set of characters with the desired length.

## License

This code is licensed under the MIT License. See the LICENSE file for details.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue on GitHub.
