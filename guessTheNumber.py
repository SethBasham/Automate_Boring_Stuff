# This is a guess the number game. 

import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# ASk the plaer o guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break # This condition is the correct answer.

if guess == secretNumber:
    print(f'Good Job! You guessed the number {guessesTaken} tries.')
else:
    print(f'Sorry. The number I was thinking of was {secretNumber}.')