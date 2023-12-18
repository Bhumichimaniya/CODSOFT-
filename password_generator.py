import random
import string

def generate_password(length):
    # Define the character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the length is at least 8 characters
    length = max(length, 8)

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    # Get user input for the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid integer for the length.")
        return

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
