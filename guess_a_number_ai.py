#Guess a number ai
#by Erik B.




import random

# config
low = 1
high = 1000
num_guess = 0


# helper functions
def show_start_screen():
    print("**************************")
    print("*  Guess a Number A.I.!  *")
    print("**************************")

def show_credits():
    print("Thank you for playing.")
    print("This awesome game was created by Erik Blom.")

def get_guess(current_high, current_low):
    return (current_high - current_low)// 2 + current_low


def pick_number():
    print("Think of a number between " + str(low) + " and " + str(high) + ".")
    print("Hit the enter key once you think of your number:")
    input()
    
def check_guess(guess):
    print("Is " + str(guess) + " your number?")
    print()
    print('Type "low" if my guess is too low')
    print('Type "high" if my guess is too high')
    print('Type "yes" if my guess is correct')
    print()
    
    while True:
        ans = input()
        if ans == 'low' or ans == 'high' or ans == 'yes':
            return ans
        else:
            print("Error: please respond with 'yes','high', or 'low'")
    print()

def show_result():
    if broke == True:
        print("Hmm, it looks like you messed up somewhere.")
    else:
        print("I guessed your number.")

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
    broke = False
    
    pick_number()
    
    while result != 'yes' and broke ==False:
        guess = get_guess(current_high, current_low)

        result = check_guess(guess)
        
        #break the loop if the the player messes up
        if(current_high - current_low)//2 == 1 and (result == 'low' or result == 'high'):
            broke = True
        if result == 'low':
            # adjust current low
            current_low = guess + 1
            #to help debug
            print("current high is " + (str(current_high)))
            print("current low is " + (str(current_low)))
            print()
 
        elif result == 'high':
            # adjust current high
            current_high = guess - 1
            #to help debug
            print("current high is " + (str(current_high)))
            print("current low is " + (str(current_low)))
            print()

    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
