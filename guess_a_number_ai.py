# Guess a number ai
#by Erik B.


import random
import math

# config
num_guess = 0
name = 'null'
intelligence = 0

# helper functions
def show_start_screen():
    print("""
             ╔═╗┬ ┬┌─┐┌─┐┌─┐  ┌─┐  ┌┐┌┬ ┬┌┬┐┌┐ ┌─┐┬─┐  ╔═╗ ╦ 
             ║ ╦│ │├┤ └─┐└─┐  ├─┤  ││││ ││││├┴┐├┤ ├┬┘  ╠═╣ ║ 
             ╚═╝└─┘└─┘└─┘└─┘  ┴ ┴  ┘└┘└─┘┴ ┴└─┘└─┘┴└─  ╩ ╩o╩o
        """)

def show_credits():
    print("""
    ╔╦╗╦ ╦╔═╗╔╗╔╦╔═╔═╗  ╔═╗╔═╗╦═╗  ╔═╗╦  ╔═╗╦ ╦╦╔╗╔╔═╗
     ║ ╠═╣╠═╣║║║╠╩╗╚═╗  ╠╣ ║ ║╠╦╝  ╠═╝║  ╠═╣╚╦╝║║║║║ ╦
     ╩ ╩ ╩╩ ╩╝╚╝╩ ╩╚═╝  ╚  ╚═╝╩╚═  ╩  ╩═╝╩ ╩ ╩ ╩╝╚╝╚═╝
     """)
    print("This awesome game was created by Erik (9-28-17).")


def pick_high():

    
    print("Hello " + name + ".")

    
    print("What do you want the highest number to be?")
    
    while True:
        high = input()
        if high.isnumeric():
            high = int(high)
            return high
        else:
            print("Please only enter a number.")

    print()
    
def pick_low():

    print("What do you want the lowest number to be?")
    
    while True:
        low = input()
        if low.isnumeric():
            low = int(low)
            return low
        else:
            print("Please only enter a number.")
            
    print()

def calc_limit(high,low):
   limit = math.log((high - low),2)
   limit = math.ceil(limit)
   return limit
    

def ask_name():
    global name
    print()
    print("First, what is your name?")
    name = input()
    print()

def dumb_guess():
    pass

def average_guess():
    pass

def perfect_guess(current_low,current_high):
    return (current_high + current_low)// 2 
   
def pick_number(limit,low,high):
    print()
    print(name + ", think of a number between " + str(low) + " and " + str(high)+ ".")
    print("Im going to guess your number in " + str(limit) + " tries or less.")
    print("Hit the enter key once you think of your number:")
    input()

def check_fault():
    pass
    
def check_guess(limit,guess,tries):
    print()
    print("Guess " + str(tries) + " of " + str(limit) +   ".")
    print(name + ", is " + str(guess) + " your number?")
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
            print(name + ", please respond with 'yes','high', or 'low'")
    print()

def show_result(tries):
    print()

    if tries == 1:
        print("I guessed your number in 1 try.")
    else:
        print("I guessed your number in " + str(tries) + " tries.")
    print()

def play_again():
    while True:
        decision = input("Would you like to play again, " + name + "? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    ask_name()
    high = pick_high()
    low = pick_low()
    
    
    current_low = low
    current_high = high
    
    limit = calc_limit(high,low)

    

    
    result = -1
    
    pick_number(limit,low,high)
    
    
    tries = 1

    error = False
    
    while result != 0:
        
        limit = calc_limit(high,low)

        guess = perfect_guess(current_high, current_low) 
            
        result = check_guess(limit,guess,tries)
        
        if tries == limit:
            if(result == -1 or result == 1):
                print("Error: You messed up answering somewhere.")
                result = 0
                error = True
            else:
                result = 0
                
        else:
            if result == -1:
                # adjust current low
                current_low = guess + 1
                print()
                tries += 1

            elif result == 1:
                # adjust current high
                current_high = guess - 1
                print()
                tries += 1
                

    if not error:
        show_result(tries)

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
