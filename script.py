import random

def makeBoard():
    board = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append("O")
        board.append(row)
    return board

def print_board(b):
    for i in b:
        print(" ".join(i))

def gameOver(result, b):
    print("\n" + result + "\nThe Game is over, thanks for playing!! \nBelow is the actual battleship deployment: \n")
    print_board(b)

class battleship(object):
    """
    This is the most tricky part of the test, I will only document this class.
    The class is designed so that any number of battleship could fit in any size a square game board.
    First decide the orientation of Battleship:
        battleship.orient = 1 means it is horizontal,
        battleship.orient = 0 means it is vertical.
    Then randomly decide the starting position of the Battleship.
        (the random range (or the board's length) of the starting point will be based on the ship's orientation.)
    Before the starting point of the Battleship is decided, the position it will take will be check if is occupied by the other ship.
    """
    def __init__(self, type, board):
        super(battleship, self).__init__()
# Define the ship's type and its length.
        if type == 1:
            self.length = 3
        if type == 2:
            self.length = 2
        boardLengthGivenOrient = len(board)-(self.length-1)
# Randomly decide the ship's orientation
        self.orient = random.randint(0,1)

#Case 1: the ship is horizontal
        if self.orient == 1:
# Set "empty" as a position occupance check: if all position the ship is going to take is empty, the while loop will stop, otherwise it will continue to find a suitable place for the ship.
            empty = self.length
            while empty > 0:
                empty = self.length
# Randomly decide the starting point of the ship.
                self.col = random.randint(0, boardLengthGivenOrient-1)
                self.row = random.randint(0, len(board)-1)
# Checking the occupance
                for i in range(self.col, self.col+self.length):
                    if board[self.row][i] == "O":
                        empty  -= 1
            for i in range(self.col, self.col+self.length):
                board[self.row][i] = "X"

#Case 2: the ship is vertical
        else:
            empty = self.length
            while empty > 0:
                empty = self.length
                self.col = random.randint(0, len(board)-1)
                self.row = random.randint(0, boardLengthGivenOrient-1)
                for i in range(self.row, self.row+self.length):
                    if board[i][self.col] == "O":
                        empty  -= 1
            for i in range(self.row, self.row+self.length):
                board[i][self.col] = "X"

    def __str__(self):
        return ("Coordinate of Ship is: " + str((self.col, self.row)))


answer = makeBoard()
gameBoard = makeBoard()
a = battleship(1, answer)
b = battleship(2, answer)

print ("\nLet's play Battleship!\nTry to find my battleship on this ocean!\n")
print_board(gameBoard)
turn = 1
while turn < 5:
    print("\nCurrent turn: " + str(turn))
    turn += 1
    gcol = int(raw_input("Guess Col:"))
    grow = int(raw_input("Guess Row:"))
    if gcol == 17 & grow == 17:
        print("\nYou enter the debug mode, \nbelow is the actual battleship deployment: \n")
        print(a)
        print(b)
        print_board(answer)
        turn -= 1

    elif answer[grow][gcol] == "X":
        result = "You Win!!"
        gameOver(result, answer)
        break
    elif gcol > 4 or grow > 4:
        print("Oops, that's not even in the ocean")
    else:
        if gameBoard[grow][gcol] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            gameBoard[grow][gcol] = "X"
    if turn < 5:
        continue
    else:
        result = "You Lose!!"
        gameOver(result, answer)
