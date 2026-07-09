import random

number = random.randint(0,9)

print("welcome to the number guessing game!")
while True:
    guess=int(input("guess a number between 0 and 9: "))
    if guess==number:
        print("congratulations! you guessed the correct number.")
        break
    else:
        print("sorry you guessed the wrong number,try again.")
        