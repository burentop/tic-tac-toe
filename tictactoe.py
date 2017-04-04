from random import randint
board = ['X', 2, 'X', 4, 5, 6, 7, 8, 9]

def display_board(board):
    start = 0
    end = 3
    for i in range(0, 3):
        print "----------"
        for j in range(start, end):
            print "|" + str(board[j]),
        print "|"
        start += 3
        end += 3
    print "----------"

def player_input(player):
    correctInput = False
    while not correctInput:
        print "Player " + player + ", please enter your move."
        print "Enter the number of a square not already occupied:"
        move = raw_input()
        if move.isdigit():
            if int(move) in board:
                correctInput = True
                board[int(move) - 1] = player
            else:
                print "That is not a valid move."
        else:
            print "That is not a valid move. Enter the number of the square."

def win_check(mark):
    if mark == board[0] and mark == board[1] and mark == board[2]:
        return True
    elif mark == board[3] and mark == board[4] and mark == board[5]:
        return True
    elif mark == board[6] and mark == board[7] and mark == board[8]:
        return True
    elif mark == board[0] and mark == board[3] and mark == board[6]:
        return True
    elif mark == board[1] and mark == board[4] and mark == board[7]:
        return True
    elif mark == board[2] and mark == board[5] and mark == board[8]:
        return True
    elif mark == board[0] and mark == board[4] and mark == board[8]:
        return True
    elif mark == board[2] and mark == board[4] and mark == board[6]:
        return True
    else:
        return False

def choose_first():
    first = randint(1, 2)
    if first == 1:
        return "X"
    else:
        return "Y"

player = choose_first()
display_board(board)
player_input(player)
display_board(board)
print win_check(player)
