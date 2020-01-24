import sys
import numpy as np

DIM = 100
TURNS = 100

#
# Get the states of all neighbouring lights
#
def neighbourStates(board, row, col):

    neighbors = []

    # Neighbors one row up
    if row > 0:
        neighbors.append(board[row-1, col])
        if col > 0:
            neighbors.append(board[row-1, col-1])
        if col < (DIM-1):
            neighbors.append(board[row-1, col+1])

    # Neighbors one row down
    if row < (DIM-1):
        neighbors.append(board[row+1, col])
        if col > 0:
            neighbors.append(board[row+1, col-1])
        if col < (DIM-1):
            neighbors.append(board[row+1, col+1])

    # Neighbors on same row
    if col > 0:
        neighbors.append(board[row, col-1])
    if col < (DIM-1):
        neighbors.append(board[row, col+1])

    return neighbors

    
#
# Get the next state for a light based on the neighboring lights
#
def nextState(board, row, col):

    on = board[row, col]
    neighbors = neighbourStates(board, row, col)

    if on:
        return sum(neighbors) == 2 or sum(neighbors) == 3
    else:
        return sum(neighbors) == 3

#
# Run one step of the simulation of entire board according to the rules.
# Return the resulting board.
#
def simulate(board):

    next_board = np.zeros(shape = (DIM, DIM), dtype = bool)

    for row in range(0, DIM):
        for col in range(0, DIM):
            next_board[row, col] = nextState(board, row, col)

    return next_board

#
# For debugging
#
def printboard(board):
    for row in range(0, board.shape[0]):
        for col in range(0, board.shape[1]):
            if board[row,col]:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')
    sys.stdout.write('\n')
    sys.stdout.flush()

#
# Set corners on (part 2)
#
def corners_on(board):
    board[0,0] = True
    board[DIM-1,DIM-1] = True
    board[0,DIM-1] = True
    board[DIM-1,0] = True

    return board

#
# Run the simulation, either with or without stuck corners
#
def solve(board, stuck_corners = False):
    tmp = board
    for _ in range(0, TURNS):
        if stuck_corners:
            tmp = corners_on(simulate(corners_on(tmp)))
        else:
            tmp = simulate(tmp)
    
    return tmp


# Build the 100 x 100 matrix with states from input (initial configuration)
board = np.zeros(shape = (DIM, DIM), dtype = bool)
rownum = 0; colnum = 0
for row in sys.stdin:
    for col in row.strip('\n'):
        if col == '#':
            board[rownum, colnum] = 1
        else:
            board[rownum, colnum] = 0
        colnum += 1
    rownum += 1
    colnum = 0

# Count the number of lamps which are on
print("Part 1: {}".format(np.sum(solve(board))))
print("Part 2: {}".format(np.sum(solve(board, True))))