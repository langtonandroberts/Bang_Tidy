
#This file is a numbers guessing game that uses Random & Randint.
#this can be used for a ruelet wheel code, just link random number to a video file.

import random 

print ('Hello. What is your name?.')
name=input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
secretNumber=random.randint(1,20)

#print('DEBUG: Secret number is '+ str(secretNumber))

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess=int(input())
    
    if guess < secretNumber:
        print('Your guess is to low.')
    elif guess > secretNumber:
        print('Your guess is to high.')
    else:
        break #this condition is for the correct guess!
    
if guess == secretNumber:
    print('Good Job,' + name + '! You guessed the correct number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


