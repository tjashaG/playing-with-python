import random

SECRET = random.randint(1, 100)
number_of_guesses = 7
guess = None

print("Welcome, player! In this game you will guess a number between 1 and 100.\nYou will have 7 guesses! Use them wisely!")


while number_of_guesses != 0:
    guess = int(input("Guess a number between 1 and 100: "))
   
    while guess < 0 or guess > 100:
        print("Please input a number within the valid range!")
        guess = int(input("Guess a number between 1 and 100: "))

    number_of_guesses -= 1
    print(f"You have {number_of_guesses} guesses remaining!")

    if guess == SECRET:
        print(f"You guessed correctly! The number was {SECRET}! You win!")
        break
    elif guess > SECRET:
        print("Not correct, but try a lower number!")
    elif guess < SECRET:
        print("Not correct, but next time aim higher!")
