# Printing the board
import random


board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

# printing the board positions
def printBoard():
    print(board[0],'|',board[1],'|',board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])
   # print('---------')

# Code for players Move
def playerTurn():
    # print('Player:')
    pos = int(input('Player:'))

    if board[pos] != 'x' and board[pos] != 'o':
        board[pos] = 'x'
    else:
        print("Already taken")

# Code for computers move
def compTurn():
    while True:
        pos = random.randint(0, 8)
        if board[pos] != 'x' and board[pos] != 'o':
            board[pos] = 'o'
            break



printBoard()

# Defining who goes first, Player or Computer
rand = random.randint(0,1)
if rand == 0:
    print("Player First")
    for i in range(1,9):
        playerTurn()
        compTurn()
        printBoard()

if rand == 1:
    print("Computer First")
    for i in range(1,9):
        playerTurn()
        compTurn()
        printBoard()




