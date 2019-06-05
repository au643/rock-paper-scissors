# game.py
#you have to import a module 
import random

print("Rock, Paper, Scissors, Shoot!")

#Capture inputs

user_choice = input ("please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes)")

print ("-------")
print ("User Choice:", user_choice)
#validate inputs
if user_choice not in ["rock", "paper", "scissors"]:
    print ("invalid selection, please try again...")
    exit()

#generate computer selection
print ("generating")

computer_choice = random.choice (["rock", "paper", "scissors"])

print ("-------")
print ("computer_choice:", computer_choice)

#determine the winner


#display final outputs / outcomes

