
import math
import random

high = 100
low = 0

limit = 0


def splash_screen():
    print(""" _____                        ___    _   _                 _               
|  __ \                      / _ \  | \ | |               | |              
| |  \/_   _  ___  ___ ___  / /_\ \ |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| |  _  | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | | | | | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/ \_| |_/ \_| \_/\__,_|_| |_| |_|_.__/ \___|_|   
                                                                           """)

def choose_bound():
    global high
    global low
    print("What will the highest number be?")
    high = int(input())
    print("What will the lowest number be?")
    low = int(input())

   
def get_limit():
    global limit
    limit = math.log(high,2);
    limit = math.ceil(limit)
    print("You are limited to " + str(limit) + " tries.")
    print()
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".")
    print()
    return random.randint(low,high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    print()

def show_result(guess,rand):
    if guess == rand:
        print("Congrats you win!")
    else:
        print("Sorry, you lose, the number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("would you like to play again? (y/n) ")

        if decision.lower() == 'y' or decision.lower() == 'yes' :
            print()
            return True
        elif decision.lower() == 'n' or decision.lower() == 'no':
            print()
            return False
        else:
            print("Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()

    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess,rand)

        tries += 1

    show_result(guess,rand)
    
splash_screen()



playing = True

while playing:
    choose_bound()
    get_limit()
    play()
    playing = play_again()

