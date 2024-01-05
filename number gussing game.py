import random

def get_user_input():
    try:
        guess = int(input("Enter any number: "))
        return guess
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input()

def play_game():
    n = random.randrange(1, 10)
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        guess = get_user_input()

        if guess < n:
            print("Too low. Try again.")
        elif guess > n:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed it right in {attempts + 1} attempts.")
            return

        attempts += 1

    print(f"Sorry, you've reached the maximum number of attempts. The correct number was {n}.")

if __name__ == "__main__":
    play_game()