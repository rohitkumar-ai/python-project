import random
import string

# Function to generate a random password
def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for strong passwords.")
        return None
    
    # Characters for password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure the password has at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with random characters from all sets
    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the list to ensure randomness and convert to string
    random.shuffle(password)
    return ''.join(password)

# Main function to take user input
def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the length of the password (minimum 4): "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
