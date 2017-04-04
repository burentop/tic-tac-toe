board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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

display_board(board)
player_input("X")
display_board(board)
