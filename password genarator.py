import random
import string

def generate_password(length):
    # Define the character set for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6 characters): "))
            if length < 6:
                print("Please enter a length of at least 6 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password: {password}")

# Run the password generator
if __name__ == "__main__":
    main()