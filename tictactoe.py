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

display_board(board)
