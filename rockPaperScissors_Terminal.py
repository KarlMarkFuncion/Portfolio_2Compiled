#This is a rock paper scissors game in the terminal of python

def myGameTakeCode():
    import random, sys

    """def randomAIMoveset():
           randNumber = random.randint(1, 3)
           if randNumber == 1:
               computerMove = "r"
               print("ROCK")
           if randNumber == 2:
               computerMove = "p"
               print("PAPER")
           if randNumber == 3:
               computerMove = "s"
               print("SCISSORS")
           return computerMove

       possibleMoves = ("rock Rock ROCK paper Paper PAPER scissors Scissors SCISSORS").split()"""

    print("ROCK, PAPERS, SCISSORS!")

    # tallies the score of the player
    wins = 0
    losses = 0
    ties = 0

    while True:  # loop of the main game
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        while True:
            print("Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit: ")
            playerMove = input()  # asks for player's moves
            if playerMove == 'q':
                sys.exit()  # closes the program
            #if playerMove == ('r', 's', 'p'):
            if playerMove == 'r' or playerMove == 's' or playerMove == 'p':
                break  # Breaks out of the input loops, excecutes to next step
                print("Please type a valid input, p/r/s/q")

        # This'll display what the chosen input was:
        if playerMove == 'r':
            #playerMove = 'r'
            print("ROCK versus...")
        elif playerMove == 'p':
            #playerMove = 'p'
            print("PAPER versus...")
        elif playerMove == 's':
            #playerMove = 's'
            print("SCISSORS versus...")

        randNumber = random.randint(1, 3)
        if randNumber == 1:
            computerMove = "r"
            print("ROCK")
        if randNumber == 2:
            computerMove = "p"
            print("PAPER")
        if randNumber == 3:
            computerMove = "s"
            print("SCISSORS")

        # Results analysis and final TALLY
        if playerMove == computerMove:
            print("It's a tie!")
            ties = ties + 1
        elif playerMove == 'r' and computerMove == 'p':
            print("COMPUTER WINS!")
            losses = losses + 1
        elif playerMove == 'p' and computerMove == 's':
            print("COMPUTER WINS!")
            losses = losses + 1
        elif playerMove == 's' and computerMove == 'r':
            print("COMPUTER WINS!")
            losses = losses + 1
        elif playerMove == 's' and computerMove == 'p':
            print("YOU WIN!")
            wins = wins + 1
        elif playerMove == 'r' and computerMove == 's':
            print("YOU WIN!")
            wins = wins + 1
        elif playerMove == 'p' and computerMove == 'r':
            print("YOU WIN!")
            wins = wins + 1

def gameOriginalCode():
    import random, sys

    print('ROCK, PAPER, SCISSORS')

    # These variables keep track of the number of wins, losses, and ties.
    wins = 0
    losses = 0
    ties = 0

    while True:  # The main game loop.
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        while True:  # The player input loop.
            print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
            playerMove = input()
            if playerMove == 'q':
                sys.exit()  # Quit the program.
            if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
                break  # Break out of the player input loop.
            print('Type one of r, p, s, or q.')

        # Display what the player chose:
        if playerMove == 'r':
            print('ROCK versus...')
        elif playerMove == 'p':
            print('PAPER versus...')
        elif playerMove == 's':
            print('SCISSORS versus...')

        # Display what the computer chose:
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = 'r'
            print('ROCK')
        elif randomNumber == 2:
            computerMove = 'p'
            print('PAPER')
        elif randomNumber == 3:
            computerMove = 's'
            print('SCISSORS')

        # Display and record the win/loss/tie:
        if playerMove == computerMove:
            print('It is a tie!')
            ties = ties + 1
        elif playerMove == 'r' and computerMove == 's':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'p' and computerMove == 'r':
            print('You win!')
            wins = wins + 1
        elif playerMove == 's' and computerMove == 'p':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'r' and computerMove == 'p':
            print('You lose!')
            losses = losses + 1
        elif playerMove == 'p' and computerMove == 's':
            print('You lose!')
            losses = losses + 1
        elif playerMove == 's' and computerMove == 'r':
            print('You lose!')
            losses = losses + 1

myGameTakeCode()