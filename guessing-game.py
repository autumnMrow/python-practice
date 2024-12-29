import math
import random

random.seed()

low = high = ""
while (low == high):
    try:
        bound1 = int(input("Provide integer bounds for the random number:\n"))
        bound2 = int(input(""))
    except ValueError:
        print("Invaliid input.")
        continue
    else:
        if (bound1 == bound2):
            continue
        else:
            low = min(bound1, bound2)
            high = max(bound1, bound2)
            break

counter = 0
attempts = int(math.log2(high - low + 1))
answer = random.randint(low, high)

guess = ""
print(f"Guess a number between: [ {low}, {high} ]")
while True:
    try:
        guess = int(input())
    except ValueError:
        print("Invalid input.")
        continue
    else:
        if guess == answer:
            print(f"Correct! You guessed in {counter + 1} tries.")
            break
        elif attempts == 0:
            print(f"No more guesses; you lose!\nThe number was {answer}.")
            break
        else:
            if guess < answer: print(f"Guess higher! You have {attempts} tries.")
            else: print(f"Guess lower! You have {attempts} tries.")
            counter += 1
            attempts -= 1
            continue
raise SystemExit