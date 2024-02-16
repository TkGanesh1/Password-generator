import random
import string

def generate_password(length=12):
    # Define character sets for password generation
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Secure Password Generator!")
    print("")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")

    # Get user input for number of passwords to generate
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")

    # Generate and display passwords
    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        password = generate_password(length)
        print(password)

if __name__ == "__main__":
    main()
