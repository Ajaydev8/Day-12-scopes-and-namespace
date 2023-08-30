import random

EASY = 10
HARD = 5

print("Welcome to the number guessing game!")

print("I'm thinking of a number in between 1 and 100")
random_number = random.randint(1, 100)


def high_or_low(guessed_number):
    if guessed_number > random_number:
        print("Too high")
    elif guessed_number < random_number:
        print("Too low")

lives = 0

user_choice = input("Choose a difficulty type 'easy' or 'hard': ").lower()


if user_choice == 'easy':
    lives = EASY
elif user_choice == 'hard':
    lives = HARD

is_on = True

while is_on:
    print(f"You have {lives} attempts remaining.")
    user_guess = int(input("Guess a number between 1 and 100: "))


    if user_guess == random_number:
        print(f"Hooray! you guessed the number correct {random_number}")
    elif user_guess != random_number:
        high_or_low(guessed_number=user_guess)
        lives -= 1
        if lives == 0:
            print(f"You ran out of attempts the number was {random_number}")
            is_on = False


