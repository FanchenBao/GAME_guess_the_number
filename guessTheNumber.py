'''
Author: Fanchen Bao
Date: 05/01/2018

Description: 
A simple game allowing users to guess the number randomly generated by the program.
User has default six chances to guess the number. The default random number range is 1 to 20 inclusive.
'''

from random import randint

# banner
print('I am thinking of a number between 1 and 20.\nYou have 6 chances to guess it.')

# range for random number generation
UPPERBOUND = 20
LOWERBOUND = 1

MAX_ATTEMPTS = 6

answer = randint(LOWERBOUND, UPPERBOUND) # generate a random answer
attempt = 0

while attempt < MAX_ATTEMPTS:
	print('Take a guess.')
	attempt += 1
	try:
		guess = int(input())
	except ValueError:
		print('Please enter an integer number.')
		continue
	if guess == answer:
		print('Good job! You guessed my number in {} guesses.'.format(str(attempt)))
		break
	elif guess < answer:
		print('Your guess is too low')
		continue
	else:
		print('Your guess is too high')
		continue

if attempt == MAX_ATTEMPTS: # max attempt limit reached
	print('Sorry, you have used all your chances. The number I am thinking of is {}.'.format(str(answer)))