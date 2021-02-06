""" Rock-paper-scissors-lizard-Spock Game 
original code: http://www.codeskulptor.org/#user48_D7hhLmv4CEq2Ny2.py
"""

""" This is my way of solving the first mini-projected given in the MOOC:

An Introduction to Interactive Programming in Python (Part 1)

https://www.coursera.org/learn/interactive-python-1

"""

"""
The mini-project is to build a the popular Rock-paper-scissors-lizard-Spock game in Python

You are provided an template and plenty of great help in the course :) 

Everything copied is marked with ##

"""

git remote add origin https://github.com/FrederikGylling/VSCode.git
git branch -M main
git push -u origin main

## The key idea of this program is to equate the strings
## "rock", "paper", "scissors", "lizard", "Spock" to numbers
## as follows:

## 0 - rock
## 1 - Spock
## 2 - paper
## 3 - lizard
## 4 - scissors

## helper functions
# it's great to first understand the problem and then divided into smaller tasks
# the problem is divided into one mainn funciton and 2 helper functions

import random

# helper funciton 1: converts input name to number based on above logic
def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else: 
        print ("choose a valid weapon")

# helper funciton 1: converts input number to name based on above logic
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print ("error: number to name")

# the game is on! 
# the computer chooses by random and the winner is choosen
def rpsls(player_choice): 
    
    # print a blank line 
    print()

    # print out the message for the player's choice
    print (("You choose ") + (player_choice))
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange( 0 , 5 )
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name( comp_number )
    
    # print out the message for computer's choice
    print (("Computer chooses ") + (comp_choice))
       
    # compute difference of comp_number and player_number modulo five
    diff = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if diff == 0:
        print ("Tie!")
    elif diff == 1 or diff == 2:
        print ("You win!")
    elif diff == 3 or diff == 4:
        print ("You loose - better luck next time!")
    else:
        print ("who is the winner?")

    # print a space after to
    print() 

# join the game, insert your choices below :) 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
