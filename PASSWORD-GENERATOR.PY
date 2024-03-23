import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase_letters = string.ascii_lowercase
        self.uppercase_letters = string.ascii_uppercase
        self.digits = string.digits
        self.special_characters = string.punctuation

    def generate_password(self, length=12):
        all_characters = self.lowercase_letters + self.uppercase_letters + self.digits + self.special_characters

        if length < 8:
            print("Password length should be at least 8 characters for better security.")
            return None

        password = random.sample(all_characters, length)
        return ''.join(password)

def main():
    password_generator = PasswordGenerator()

    print("Welcome to the Password Generator!")
    password_length = int(input("Enter the desired length for your password: "))

    generated_password = password_generator.generate_password(password_length)

    if generated_password:
        print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()
