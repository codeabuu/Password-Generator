# Random Password Generator

This Python script generates a random password consisting of letters (both uppercase and lowercase) and symbols. The password has a length of 8 characters, with 5 random letters and 3 random symbols.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository or download the `password_generator.py` file.
3. Run the script by executing the command `python password_generator.py`.
4. The generated password will be displayed on the console.

## How It Works

1. The script initializes an empty string `password_chars` to store the possible characters for the password.
2. It iterates over the ASCII range for uppercase letters (A-Z) and lowercase letters (a-z) and appends them to `password_chars`.
3. A list of symbols is defined.
4. The script generates a random sample of length 8 from `password_chars` using the `random.sample()` function. This ensures a mix of uppercase and lowercase letters.
5. It adds 2 random symbols from the symbol list to the password.
6. The password characters are shuffled randomly in-place using `random.shuffle()`.
7. The characters are joined together to form a string, resulting in the generated password.
8. The password is displayed on the console.

## Customization

- To change the length of the password, modify the `k` argument in `random.sample(password_chars, k=8)` and adjust it to the desired length.
- You can modify the list of symbols to include or exclude specific symbols as per your requirements.

Feel free to use this code as a starting point and customize it further to meet your specific password generation needs.
