import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    tries = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        tries += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! The number was {number_to_guess}. It took you {tries} tries.")
            break

number_guessing_game()
