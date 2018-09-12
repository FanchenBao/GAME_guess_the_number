from random import randint

print('I am thinking of a number between 1 and 20.\nYou have 6 chances to guess it.')

answer = randint(1, 20)
attempt = 0

while attempt < 6:
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

if attempt == 6:
	print('Sorry, you have used all your chances. The number I am thinking of is {}.'.format(str(answer)))