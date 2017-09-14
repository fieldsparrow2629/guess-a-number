import random

high = 100
low = 1
limit = 10

rand = random.randrange(low,high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1
tries = 0

while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    tries += 1
    print("You have " + str(limit - tries) + " tries left.")


if tries == limit:
    print("You lose.")
else:
    print("You win.")
