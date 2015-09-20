#Info 206
#Place-in exam
#Example 3


# imports
from random import randint


# body
def print_board(board):
    for row in board:
        print " ".join(row)

def get_ship_coords(num):
    """This function takes the length of a ship as an argument, chooses a random horz/vert 
    orientation and coordinates, and returns a list of tuples with those coordinates."""
    # determine whether ship will be horizontal or vertical
    orientation = randint(0,1)
    ship_coords = []
    if orientation == 0:            # this will be horz
        # if horizontal, ship can only start in columns 0 to (5-num)
        # but can be in any row on the board
        x_start, y_start = randint(0,(5-num)), randint(0,4)
        for count in range(num):
            ship_coords.append((x_start + count, y_start))
    else:
        # if vertical, ship can only start in rows 0 to (5-num)
        # but can be in any column on the board
        x_start, y_start = randint(0,4), randint(0,(5-num))
        for count in range(num):
            ship_coords.append((x_start, y_start + count))
    return ship_coords

def check_overlap(coords1, coords2):
    for item in coords2:
        if item in coords1:
            return True

def user_guesses(ship1, ship2, board):
    """This function takes two lists of tuples as arguments, then takes user input and compares
    it to those tuple lists to see if the user guessed correctly."""
    turn = 0
    while turn < 4:       # Give the player 4 guesses
        print "\nTurn", turn + 1
        try:
            #let the user guess a set of coordinates
            guess_col = int(raw_input("Guess column: "))
            guess_row = int(raw_input("Guess row: "))
        except Exception:
            print "You must enter an integer."  # I won't penalize them on turns for this
            pass
        else:
            turn += 1
            # if they give the secret handshake:
            if guess_row == 17 and guess_col == 17:
                print_debug(ship1, ship2)
                turn -= 1
            # if they guess outside the range of board coordinates
            elif guess_row not in range(5) or guess_col not in range(5):
                print "Oops, that's not even in the ocean."
                pass
            # compare their guess against the two lists of tuples (the ship coords)
            elif (guess_col, guess_row) in ship1 or (guess_col, guess_row) in ship2:
                print "Congratulations! You sank my battleship!"
                break
            else:
                # check against previous guesses to the original board
                if board[guess_row][guess_col] == "X":
                    print "You guessed that one already."
                else:
                    print "You missed my battleship!"
                    # mark their guesses on the board
                    board[guess_row][guess_col] = "X"
                print_board(board)
        if turn == 4:
            print "\nGame Over\n"

def print_debug(ship1, ship2):
    """This will print the locations of the battleships, with "1" in the coords where the 3x1
    ship is, and "2" in the coords where the 2x1 ship is."""
    ship_board = [["O"]*5 for x in range(5)]
    # fill out the board with the ship coordinates
    for coord in ship1:
        # I have them saved as (column, row) but need to print out by row then by column
        ship_board[coord[1]][coord[0]] = "1"         
    for coord in ship2:
        ship_board[coord[1]][coord[0]] = "2"
    print_board(ship_board)


def battleship():
    game_board = [["O"]*5 for x in range(5)]
    print "\nLet's play Battleship! You have four chances to sink my ships."
    ship1 = get_ship_coords(3)     # get coords for a 3x1 ship
    ship2 = get_ship_coords(2)     # get coords for a 2x1 ship
    while check_overlap(ship1, ship2) == True:  # if they overlap, try another combination
        ship2 = get_ship_coords(2) 
    user_guesses(ship1, ship2, game_board)


# main function
def main():
    battleship()

if __name__ == '__main__':
    main()