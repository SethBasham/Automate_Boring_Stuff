import random, sys

print('\nThe Game of Rock, Paper, Scissors \n')

# These variables keep track of the number of wins, losses and ties.

wins = 0
losses = 0
ties = 0

for i in range(1, 100):

    while True: # The main game loop.
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        while True: # The player input loop.
            print('Enter your move: [R]ock, [P]aper, [S]cissors or [Q]uit')
            playerMove = input().capitalize()
            if playerMove == 'Q':
                sys.exit() # Quit the program.
            if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
                break # Break out of the player input loop.
            print('Type R, P, S or Q.')

        # Display what the player chose.
        if playerMove =='R':
            print(f'Rock VERSUS ...')
        if playerMove == 'P':
            print('Paper VERSUS ...')
        if playerMove == 'S':
            print('Scissors VERSUS ...')

        # Display what the computer chose.
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = 'R'
            print('Rock')
        if randomNumber == 2:
            computerMove = 'P'
            print('Paper')
        if randomNumber == 3:
            computerMove = 'S'
            print('Scissors')

        # Display and record the win, loss, and ties.
        if playerMove == computerMove:
            print('It is a Tie! \n')
            ties += 1 
        elif playerMove == 'R' and computerMove == 'S':
            print('You Win! \n')
            wins += 1
        elif playerMove == 'P' and computerMove == 'R':
            print('You Win! \n')
            wins += 1
        elif playerMove == 'S' and computerMove == 'p':
            print('You Win! \n')
            wins += 1
        elif playerMove == 'R' and computerMove == 'P':
            print('You Lose! \n')
            losses += 1
        elif playerMove == 'P' and computerMove == 'S':
            print('You Lose! \n')
            losses += 1
        elif playerMove == 'S' and computerMove == 'R':
            print('You Lose! \n')
            losses += 1