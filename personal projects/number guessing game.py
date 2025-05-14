import random
import math

print("welcome to my number guessing game")
print("you are going to guess the number i pick with a limited number of trials")
print("")

while True:
    lower_bound = int(input("enter a lower bound number for the starting range: "))
    upper_bound = int(input("enter a upper bound number for the ending range: "))
    if upper_bound <= lower_bound:
        print("upperbound number cannot be less than or equal lower bound")
        continue
    else:
        break

random_integer = random.randint(lower_bound, upper_bound)
user_trials = round(math.log2(upper_bound - lower_bound + 1))
print("i have selected a number from the range you gave me")
print(f"now you have {user_trials} guesses to guess the number i picked")
a = 0
print(random_integer)

while a <= user_trials-1:
    a = a + 1
    user_pick = int(input(f"Trial {a}: enter your guess: "))

    if user_pick > random_integer:
        print("you guessed to high, try again...")
        continue
    elif user_pick < random_integer:
        print("you guessed to small, try again... ")
        continue
    else:
        print("congratulations, you guessed right")
        break


if a >= user_trials:
    print("better luck next time")
else:
    print("thank you for playing")
