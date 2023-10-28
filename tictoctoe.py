import random
board=[[1,2,3],[4,5,6],[7,8,9]]
player_choice = ''

def display_board(board):
    
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------" * 3,"+", sep="")
    for row in range(3):
            print("|       " * 3,"|", sep="")
            for col in range(3):
                print("|   "+str(board[row][col])+"   ", end="")
        
            print("|")
            print("|       " * 3,"|",sep="")
            print("+-------" * 3,"+",sep="")
    

# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
def make_list_of_free_fields(board,player_choice,pc_choice):
    # The function browses the board and builds a list of all the free squares; 
    # The list consists of tuples, while each tuple is a pair of row and column numbers.
    # arggggx

    
    for free in board:
        if str(free) !=  player_choice or pc_choice:
            print('this are open')
            open_space = []
            open_space.append(free)
            o = tuple(open_space)
            print(*o,end=' ')
    print('')

def draw_PCs_move(pc_choice):
    # The function draws the computer's move and updates the board.
    # while True:
        pc_move = random.randint(1,9)
    
        if pc_move == 1:
            board[0][(pc_move-1)]= pc_choice
        if pc_move == 2:
            board[0][(pc_move-1)]= pc_choice
        if pc_move == 3:
            board[0][(pc_move-1)]= pc_choice

        if pc_move == 4:
            board[1][(pc_move-4)]= pc_choice
        if pc_move == 5:
             board[1][(pc_move-4)]= pc_choice
        if pc_move == 6:
            board[1][(pc_move-4)]= pc_choice

        if pc_move == 7:
            board[2][(pc_move-7)]= pc_choice
        if pc_move == 8:
            board[2][(pc_move-7)]= pc_choice
        if pc_move == 9:
            board[2][(pc_move-7)]= pc_choice
        # print('\n')
        print(f"**The PC has made its move, it has taken {pc_move}**\n")
        display_board(board)

def enter_move(player_choice):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    player_choice = ''
    print('\n')
    if player_choice == '':
            sign = str(input("Are you 'X' or are you 'O': ")).capitalize()
            print('')

            if sign == 'X':
                player_choice = 'X'
                pc_choice = 'O'

                print(f"You have taken {player_choice} The PC will take {pc_choice}\n")
                
            elif sign == 'O':
                player_choice = 'O'
                pc_choice = 'X'

                print(f"You have taken {player_choice} The PC will take {pc_choice}\n")


            elif sign != 'X' or 'O':
                print("Sorry  player we only accept 'O' or 'X' here! Try again...\n")
            
    

    while True:  
            move = int(input(f"Where do you want to put your {player_choice}: "))
            
            if move == 1:
                board[0][(move-1)]= player_choice
            if move == 2:
                board[0][(move-1)]= player_choice
            if move == 3:
                board[0][(move-1)]= player_choice

            if move == 4:
                board[1][(move-4)]= player_choice
            if move == 5:
                board[1][(move-4)]= player_choice
            if move == 6:
                board[1][(move-4)]= player_choice

            if move == 7:
                board[2][(move-7)]= player_choice
            if move == 8:
                board[2][(move-7)]= player_choice
            if move == 9:
                board[2][(move-7)]= player_choice
            
        
            display_board(board)
            draw_PCs_move(pc_choice)
            make_list_of_free_fields(board,player_choice,pc_choice)  

            


def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # if board list spaces equal = x,x,x you win
    pass


        

def play():
    print("Welcome to Michi Ticktocktoe game")       
    display_board(board)
    enter_move(player_choice)


while True:
    play()