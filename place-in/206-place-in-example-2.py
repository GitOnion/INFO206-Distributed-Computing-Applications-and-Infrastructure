#Info 206
#Place-in exam
#Example 2

#!/usr/bin/env python
# Battleship game. 

# Imports
from random import randint, choice

# Body
def initialise_board(size):
    board = []
    for x in range(5):
        board.append(["O"] * size)
    return board


def print_board(board):
    for row in board:
        print " ".join(row)


def random_pos(board, size):
    """ Returns a random position of the top-left position of the ship such that the ship is still on the board."""

    return randint(0, len(board) - size)


def check_overlap(solution_board, ship_row_first, ship_col_first, size, horizontal):
    """ Check if the new boat overlaps another boat.

    Return False if there is no contact and True if there is. 
    """
    for shift in range(size):
        if horizontal == True and solution_board[ship_row_first][ship_col_first + shift] == "S":
            return True
        elif horizontal == False and solution_board[ship_row_first + shift][ship_col_first] == "S":
            return True
    return False


def place_battleship(solution_board, size):
    """ Add battleship of size "size" on a free space on the board. """

    # Select orientation
    horizontal = choice([True, False])
    if horizontal == True:
        hsize = size
        vsize = 1
    else:
        hsize = 1
        vsize = size   

    overlap = True
    while overlap:
        # Assign top left position of battleship
        ship_row_first = random_pos(solution_board, vsize)
        ship_col_first = random_pos(solution_board, hsize)

        # Check for contact
        overlap = check_overlap(solution_board, ship_row_first, ship_col_first, size, horizontal)
    
    # Modify solutions board
    for shift in range(size):
        if horizontal == True:
            solution_board[ship_row_first][ship_col_first + shift] = "S" # S stands for ship
        elif horizontal == False:
            solution_board[ship_row_first + shift][ship_col_first] = "S"
    

def validate_guess(board, solution_board, guess_row, guess_col):
    """ Validate the user input against the current board. """

    if (guess_row < 0 or guess_row > len(board) - 1) or (guess_col < 0 or guess_col > len(board) - 1):        # Test if guess is outside range
        print "Oops, that's not even in the ocean."
    elif solution_board[guess_row][guess_col] == "S":
        print "Congratulations! You sunk one of my battleship!"
        exit(1)
    elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
 

def validate_input():
    """ Prompt user for input until a valid input is obtained."""

    while 1:
        try:
            guess_row = int(raw_input("Guess Row:"))
            guess_col = int(raw_input("Guess Col:"))
        except Exception:
            print("Input is not a valid integer. Please try again.")
        else:
            break
    return guess_row, guess_col


def main():
    # Game initialisation
    board_size = 5
    board = initialise_board(board_size)
    solution_board = initialise_board(board_size)
    
    # Randomly place battleship
    place_battleship(solution_board, 3)
    place_battleship(solution_board, 2)
    
    # Game loop
    print "Let's play Battleship!"
    print_board(board)

    turn = 0
    while turn < 4:
        print("Turn {}".format(turn + 1))
        
        # Guess loop
        guess_row, guess_col = validate_input()
        
        # Debug mode
        if guess_row == 17 and guess_col == 17:
            print("Solutions")
            print_board(solution_board)
            continue
        
        # Test that guess
        validate_guess(board, solution_board, guess_row, guess_col)
        print_board(board)

        turn += 1

    # Game failure
    print "Game Over"
    exit(0)

if __name__ == "__main__":
    main()