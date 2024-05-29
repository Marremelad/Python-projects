import random
import sys
def main():

    while True:

        try:
            n = int(input("Level "))

            if n > 1:
                break
        except ValueError:
            pass

    answer = random.randint(1, n)

    print("Guess:", end = " ")
    while True:

        try:
            guess = int(input(""))

            if guess < answer:
                print("Too small!")

            elif guess > answer:
                print("Too large!")

            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            pass
main()
