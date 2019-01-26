# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:32:48 2016

@author: Mark
"""

#This is a guess the number game.
import random
secretNumber = random.randit(1, 20)
print('Iam thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break           #this condition is the correct guess!
        
if guess == secretNumber:
    print('Good Job! You guess my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))