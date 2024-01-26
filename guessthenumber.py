import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    guess = 0
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    
    while guess != secret_number:
        try:
            # Get user input for a guess
            guess = int(input("Enter your guess (between 1 and 100): "))
            
            # Increment the number of attempts
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            elif guess < secret_number:
                print("Too low! Try guessing higher.")
            else:
                print("Too high! Try guessing lower.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
if __name__ == "__main__":
    number_guessing_game()
