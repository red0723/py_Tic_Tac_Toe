from random import randrange
import signal
import sys

board = (
    ('1', '2', '3'),  # Row 0
    ('4', '5', '6'),  # Row 1
    ('7', '8', '9')   # Row 2
)

def signal_handler(sig, frame):
    print('Exiting gracefully...')
    sys.exit(0)
    
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print('+-------+-------+-------+')
    for row in board:
        print('|       |       |       |')
        print('|  ','   |   '.join(row),'  |')
        print('|       |       |       |')
        print('+-------+-------+-------+')

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    row, column = None, None
    empty_spaces = list(make_list_of_free_fields(board))
    for a in range(3):
        for b in range(3):
            if board[a][b] in empty_spaces:
                row,column = a,b
                
    if row is not None and column is not None:
        valid_move = False
        while valid_move == False:
            player = input("Enter your move: ")
            if player in empty_spaces:
                valid_move = True
                break
            else:
                player = input("Enter a valid move: ")
        for a in range(3):
            for b in range(3):
                if board[a][b] == player:
                    row,column = a,b    
        new_row = list(board[row])
        new_row[column] = 'O'
        new_row = tuple(new_row)
        new_board = list(board[:])
        new_board[row] = new_row
        display_board(new_board)
        victory_for(board, 'O')
        draw_move(tuple(new_board))
    else:
        victory_for(board, 'O')
    

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    spaces = list(board[0])#['1','2','3','4','5','6','7','8','9']
    empty_spaces = []
    spaces_available = []
    for i in spaces:
        for a in range(3):
            for b in range(3):
                space = board[a][b]
                spaces_available.append(space)
        for i in spaces_available:
            if i not in empty_spaces and i != 'X' and i != 'O':
                empty_spaces.append(i)
    return empty_spaces
        
def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    spaces_left = make_list_of_free_fields(board)
    xdiagl = 0
    odiagl = 0
    xdiagr = 0
    odiagr = 0
    xdr = 0
    odr = 0
    xdm = 0
    odm = 0
    xdl = 0
    odl = 0
    xat = 0
    oat = 0
    xam = 0
    oam = 0
    xab = 0
    oab = 0
    x_got_three = False
    o_got_three = False
    for i in reversed(range(3)):
        if board[i][i] == 'X':
            xdiagl += 1
        else:
            if board[i][i] == 'O':
                odiagl += 1
    for i in range(3):
        if board[i][i] == 'X':
            xdiagr += 1
        else:
            if board[i][i] == 'O':
                odiagr += 1
                
        if board[i][2] == 'X':
            xdr += 1
        else:
            if board[i][2] == 'O':
                odr += 1
        if board[i][1] == 'X':
            xdm += 1
        else:
            if board[i][1] == 'O':
                odm += 1 
        if board[i][0] == 'X':
            xdl += 1
        else:
            if board[i][0] == 'O':
                odl += 1 
        
        if board[0][i] == 'X':
            xat += 1
        else:
            if board[0][i] == 'O':
                oat += 1
        if board[1][i] == 'X':
            xam += 1
        else:
            if board[1][i] == 'O':
                oam += 1 
        if board[2][i] == 'X':
            xab += 1
        else:
            if board[2][i] == 'O':
                oab += 1
                
    if xdiagl == 3 or xdiagr == 3 or xdl == 3 or xdm == 3 or xdr == 3 or xat == 3 or xam == 3 or xab == 3:
        x_got_three = True        
    if odiagl == 3 or odiagr == 3 or odl == 3 or odm == 3 or odr == 3 or oat == 3 or oam == 3 or oab == 3:
        o_got_three = True 
    if ((x_got_three == True) and (o_got_three == True) and spaces_left == []) or ((x_got_three == False) and (o_got_three == False) and spaces_left == []):
        print("ITS A TIE!!!")
        sys.exit()
    elif (x_got_three == True) and (o_got_three == False):
        print("The Computer won.")
        sys.exit()
    elif  (x_got_three == False) and (o_got_three == True):
        print("You WON!!!")
        sys.exit()
    else:
        return board
    
def draw_move(board):
    # The function draws the computer's move and updates the board.
    empty_spaces = list(make_list_of_free_fields(board))
    row, column = None, None
    for a in range(3):
        for b in range(3):
                if board[a][b] == '5':
                    row, column = a,b
                    break
    if row != 1 and column != 1:
        for a in range(3):
            for b in range(3):
                if board[a][b] in empty_spaces:
                    row,column = a,b
                    break

    if row is not None and column is not None:
        new_row = list(board[row])
        new_row[column] = 'X'
        new_row = tuple(new_row)
        new_board = list(board[:])
        new_board[row] = new_row
        display_board(new_board)
        victory_for(board, 'X')
        enter_move(tuple(new_board))
    else:
        victory_for(board, 'X')

display_board(board)
board = draw_move(board)
