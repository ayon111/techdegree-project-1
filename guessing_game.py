# Please note that the project is being submitted for "Exceeds" category
import random
import sys


def start_game():
    no_of_tries = 0
    high_score = 0

    print("------------------------------")
    print("Welcome to the Number Guessing Game")
    print("------------------------------")
    solution = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Pick a number between 1 and 10: "))
        except ValueError:
            print("Please enter an integer number")
        else:
            if guess > 10 or guess < 1:
                print("You must guess a number between 1 and 10")

                continue
            elif guess > solution:
                print("Your guess is higher than the number you are supposed to guess!")
                no_of_tries += 1
                continue
            elif guess < solution:
                print("Your guess is lower than the number you are supposed to guess!")
                no_of_tries += 1
                continue
            else:
                no_of_tries += 1
                print("You got it!. It took you {} tries.".format(no_of_tries))
                high_score = no_of_tries
            while True:
                again = input("Would you like to play again?[y]es/[n]o?")
                if (again.lower() == "y"):
                    print("The HIGHSCORE is {}".format(high_score))
                    start_game()
                    break
                elif (again.lower() == "n"):
                    print("Thank you for playing the game.Good Bye")
                    sys.exit()
                else:
                    print("You must enter 'y' or 'n' to inform about your decision")
                    continue


if __name__ == '__main__':
    start_game()
