import random


#
# def guess_the_number(x):
#     print("Let's play Guess The Number")
#
#     random_number = random.randint(0, x)
#
#     num_guesses = 0
#     while True:
#         guess = int(input(f"Guess a number between 0 and {x}:"))
#         num_guesses += 1
#         if guess == random_number:
#             print(f"Congrats,the number is {random_number}")
#             break
#         elif guess < random_number:
#             print("Too low!")
#         else:
#             print("To high!")


def guess_the_number(upper_bound):
    secret_number = random.randint(1, upper_bound)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and {}".format(upper_bound)))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Cogratulations! You guessed the number{}in{}attempts.".format(secret_number, attempts))
            break
