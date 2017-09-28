#Guess a number ai
#by Erik B.




import random

# config
low = 1
high = 1000
num_guess = 0


# helper functions
def show_start_screen():
    print("""
             ╔═╗┬ ┬┌─┐┌─┐┌─┐  ┌─┐  ┌┐┌┬ ┬┌┬┐┌┐ ┌─┐┬─┐  ╔═╗ ╦ 
             ║ ╦│ │├┤ └─┐└─┐  ├─┤  ││││ ││││├┴┐├┤ ├┬┘  ╠═╣ ║ 
             ╚═╝└─┘└─┘└─┘└─┘  ┴ ┴  ┘└┘└─┘┴ ┴└─┘└─┘┴└─  ╩ ╩o╩o
        """)

def show_credits():
    print(""""
    ╔╦╗╦ ╦╔═╗╔╗╔╦╔═╔═╗  ╔═╗╔═╗╦═╗  ╔═╗╦  ╔═╗╦ ╦╦╔╗╔╔═╗
     ║ ╠═╣╠═╣║║║╠╩╗╚═╗  ╠╣ ║ ║╠╦╝  ╠═╝║  ╠═╣╚╦╝║║║║║ ╦
     ╩ ╩ ╩╩ ╩╝╚╝╩ ╩╚═╝  ╚  ╚═╝╩╚═  ╩  ╩═╝╩ ╩ ╩ ╩╝╚╝╚═╝
     """)
    print("This awesome game was created by Erik (9-28-17).")

def get_guess(current_high, current_low):
    return (current_high + current_low)// 2 


def pick_bounds():
    print("What do you want the highest number to be?")
def pick_number():
    print()
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
        ans = ans.lower()
        
        if ans == 'low' or ans == 'l' or ans == 'lower':
            return -1
        elif ans == 'high' or ans == 'h' or ans == 'higher':
            return 1
        elif ans == 'yes' or ans == 'y':
            return 0
        else:
            print("Error: please respond with 'yes','high', or 'low'")
    print()

def show_result():
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

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
        
        if result == -1:
            # adjust current low
            current_low = guess + 1
            print()
 
        elif result == 1:
            # adjust current high
            current_high = guess - 1
            print()

    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
