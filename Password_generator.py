import random
import string

# To store generated passwords and ensure they aren't repeated 
generated_passwords = set()

# Get user inputs 
while True:
    try:
        password_length = int(input("Enter the desired password length (between 6 and 256): ")) 
        if password_length < 6 or password_length > 256:
            raise ValueError("Password length must be between 6 and 256.")
        break
    except ValueError as e:
        print(f"Error: {e}")

while True:
    combination = input(
        "Enter the combination of characters (a for alphabets, d for digits, s for symbols, uc for uppercase, lc for lowercase): "
    ).strip().lower()
    
    valid_combinations = {'a', 'd', 's', 'uc', 'lc'}
    if set(combination.split()).issubset(valid_combinations) and combination:
        print("Valid combination entered.")
        break  # Exit the loop if a valid combination is entered
    else:
        print("Invalid combination. Please enter again.")

# Define the character sets based on user input
char_sets = {
    'a': list(string.ascii_letters),  # a for alphabets
    'd': list(string.digits),         # d for digits
    's': list(string.punctuation),    # s for symbols
    'uc': list(string.ascii_uppercase),  # uc for uppercase
    'lc': list(string.ascii_lowercase)  # lc for lowercase
}

# Collect all characters to be used in the password
all_characters = []
for char_type in combination.split():
    all_characters.extend(char_sets[char_type])

# Ensure at least one character from each selected set
required_characters = [random.choice(char_sets[char_type]) for char_type in combination.split()]

# Fill the rest of the password length with random characters from all selected sets
password = required_characters + random.choices(all_characters, k=password_length - len(required_characters))

# Shuffle the password to ensure randomness
random.shuffle(password)

# Convert the password list to a string
password = ''.join(password)

# Check for uniqueness and display the password 
if password not in generated_passwords: 
    generated_passwords.add(password) 
    print("Generated Password:", password)
else:
    print("Failed to generate a unique password. Please try again.")
