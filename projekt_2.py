"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lucie Dally
email: lck21@seznam.cz
discord: lucie9855
"""

import random

def generate_secret_number():
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_number = numbers[:4]
    return secret_number

def evaluate_guess(secret_number, guess):
    bulls = 0
    cows = 0

    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1

    return bulls, cows

def main():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret_number = generate_secret_number()

    attempts = 0
    while True:
        player_guess = input("Enter a number: ")

        if len(player_guess) != 4 or not player_guess.isdigit():
            print("Please enter 4 different digits.")
            continue

        player_guess = [int(digit) for digit in player_guess]
        attempts += 1

        bulls, cows = evaluate_guess(secret_number, player_guess)

        print(f"{bulls} bulls, {cows} cows")
        print("-----------------------------------------------")

        if bulls == 4:
            if attempts > 1:
                print(f"Correct, you've guessed the right number {secret_number} in {attempts} guesses!")
            break

if __name__ == "__main__":
    main()