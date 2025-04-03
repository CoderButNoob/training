import random 

def make_a_board():
    return [[' ' for _ in range(3)]for _ in range(3)]

def show_board(board):
    for row in board:
        print(row)

def user_input(board):
    while True :
        row = int(input("Enter Number between 0 to 2"))
        col = int(input("Enter number between 0 to 2"))

        #check if position is empty or not 
        if 0<=row<3 and 0<=col<3 and board[row][col]==" ":
            board[row][col]='X'
            break
        else:
            print("Cell already occupied or out of Range")

def random_move(board):
    while True:
        row = random.randint(0,2)
        col =  random.randint(0,2)

        if board[row][col]==' ':
            board[row][col] = 'O'
            break


def winner(board , user):
    for i in  range(3):
        if all(board[i][j]==user for j in range(3)): #check rows
            return True 
        if all(board[j][i]==user for j in range(3) ): #check cols
            return True
        
    if all(board[i][i]== user for i in range(3)): #Main Diagonal
        return True
    
    if all(board[i][2-i]==user for i in range(3)): #Anti Diagonal
        return True
    
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)




def play_game():
    board = make_a_board()

    

    while True:

        user_input(board)

        show_board(board)

        if winner(board,'X'):
            print("You won")
            break

        check_draw(board)

        random_move(board)
        show_board(board)

        if winner(board,'O'):
            print("You Lost")
            break 

        check_draw(board)

play_game()


