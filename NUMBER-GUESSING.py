import random

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def display_welcome_message(self):
        print("Welcome to the Number Guessing Game!")
        print("I have selected a random number between 1 and 100. Can you guess it?")

    def get_user_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play_game(self):
        self.display_welcome_message()

        while True:
            guess = self.get_user_guess()
            self.attempts += 1

            if guess == self.secret_number:
                print(f"Congratulations! You've guessed the correct number {self.secret_number} in {self.attempts} attempts.")
                break
            elif guess < self.secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

def main():
    number_game = NumberGuessingGame()
    number_game.play_game()

if __name__ == "__main__":
    main()
