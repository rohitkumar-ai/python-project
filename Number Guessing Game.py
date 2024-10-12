import random

def guess_number():
    # The computer randomly selects a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
        
if __name__ == "__main__":
    guess_number()
