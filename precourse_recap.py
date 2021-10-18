import random

min = 1
max = 10

answer = random.randint(min, max)  
guess = input("Guess a number between %d and %d: " % (min, max))

if int(guess) == answer:
    print("You were right")
else:
    print("Wrong. The answer was %d" % answer)

