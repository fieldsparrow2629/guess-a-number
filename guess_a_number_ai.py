import random

# config
low = 1
high = 1000


# helper functions
def show_start_screen():
    print("**************************")
    print("*  Guess a Number A.I.!  *")
    print("**************************")

def show_credits():
    print("This awesome game was created by Coop Dogg.")
    
def get_guess(current_high, current_low):
    x = (current_high - current_low) // 2
    return x

def pick_number():
    print("Think of a number between " + str(low) + " and " + str(high) + ".")
    print("Hit the enter key once you think of your number:")
    input()
    
def check_guess(guess):
    print("Is " + str(guess) + " your number?")
    print()
    print('Type "2" if my guess is too low')
    print('Type "1" if my guess is too high')
    print('Type "0" if my guess is correct')
    
    while True:
        ans = int(input())
        if ans == 2 or ans == 1 or ans == 0:
            return ans
        else:
            print("Error: please respond with 1,-1, or 0")

def show_result():
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    result = -1
    
    pick_number()
    
    while result != 0:
        guess = get_guess(current_high, current_low)

        result = check_guess(guess)

        if result == 2:
            # adjust current low
            current_low = guess + 1
            print("current high is " + (str(current_high)))
            print("current low is " + (str(current_low)))
 
        elif result == 1:
            # adjust current high
            current_high = guess - 1
            print("current high is " + (str(current_high)))
            print("current low is " + (str(current_low)))    

    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
