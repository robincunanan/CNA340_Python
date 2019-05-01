import random
RandomNumber = random.randint(1,10)

Guess = int(input("I'm thinking of an number between 1 and 10. You have three guesses. "))
if Guess == RandomNumber:
    print("That's correct! The number was ", RandomNumber)
else:
    if Guess > RandomNumber:
        Guess = int(input("Your number was too high! Try again. This is your second guess: "))
    elif Guess < RandomNumber:
        Guess = int(input("Your number was too low! Try again. This is your second guess: "))
if Guess == RandomNumber:
    print("That's correct! The number was ", RandomNumber)
else:
    if Guess > RandomNumber:
        Guess = int(input("Your number was too high! Try again. This is your third guess: "))
    elif Guess < RandomNumber:
        Guess = int(input("Your number was too low! Try again. This is your third guess: "))
if Guess == RandomNumber:
    print("That's correct! The number was ", RandomNumber)
else:
    if Guess > RandomNumber:
        print("You lose! Your number was too high! The number was", RandomNumber)
    elif Guess < RandomNumber:
        print("You lose! Your number was too low! The number was", RandomNumber)

print("Done")
