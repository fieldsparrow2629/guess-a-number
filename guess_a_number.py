import random

high = 100
low = 1
limit = 10

#intro to game
rand = random.randrange(low,high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1
tries = 0

#main game loop
while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
        
    tries += 1
    print("You have " + str(limit - tries) + " tries left.")


#game ends
if tries == limit:
    print("You lose. The number was " + str(rand) + ".")
else:
    print("You win.")
