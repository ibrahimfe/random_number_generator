import string
import random
import argparse

# Merekam Argument yang ada di command line
parser = argparse.ArgumentParser(description="Generater A Random Password")
parser.add_argument(
    "length", type=int, default=8, help="Length of The Password, default is 8"
)
parser.add_argument(
    "-p", "--punctuation", action="store_true", help="Include Punctuation"
)
parser.add_argument("-n", "--number", action="store_true", help="Include Numbers")
args = parser.parse_args()

# Menginisialisasikan sets dari karakter
lowercase_letter = string.ascii_lowercase
uppercase_letter = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

# Default Karakter
character = lowercase_letter + uppercase_letter

# Opsi Penambahan Angka dan Special Karakter
if args.number:
    character += digits
if args.punctuation:
    character += punctuation

# Generate Password
password = "".join(random.choice(character) for _ in range(args.length))

print(password)
