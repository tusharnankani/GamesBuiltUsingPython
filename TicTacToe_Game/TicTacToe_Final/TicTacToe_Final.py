####	TIC TAC TOE 	####
##	  Tushar Nankani 	##

'''
Specifications:
2 players will be able to play the game (both sitting at the same computer);
The board will be printed out every time a player makes a move
'''

#START;


#FUNCTIONS;

def default():
    print("\nWelcome to Tushar's TIC TAC TOE!\n")


def rules():
    print("The board will look like this!")
    print("The positions of this 3 x 3 board is same as the right side of your key board.\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\nYou just have to input the position(1-9).")


def play():
    play=input("Are you ready to play the game? Enter Yes or No.\t")[0].upper()
    return play=='Y'


def names():
    #Player names input;
    
    p1_name=input("\nEnter NAME of PLAYER 1:\t").capitalize()
    p2_name=input("Enter NAME of PLAYER 2:\t").capitalize()
    return (p1_name,p2_name)


def choice():
    #Player choice input;
    p1_choice = ' '
    p2_choice = ' '
    while p1_choice != 'X' or p1_choice != 'O':          #while loop; if the entered value isn't X or O;
        
        #WHILE LOOP STARTS

        p1_choice = input(f"\n{p1_name}, Do you want to be X or O?\t")[0].upper()
        #The input above has [0].upper() in the end;
        #So the user can enter x, X, xxxx or XXX; the input will always be taken as X;
        #Thereby, increasing the user input window;

        if p1_choice == 'X' or p1_choice == 'O':
            #if entered value is X or O; get out of the loop; 
            break
        print("INVALID INPUT! Please Try Again!") 
        #if the entered value isn't X or O, re-run the while loop;

        #WHILE LOOP ENDS
    #Assigning the value to p2 and then diplaying the values;
    if p1_choice == 'X':
        p2_choice = 'O'
    elif p1_choice == 'O':
        p2_choice = 'X'
    
    return (p1_choice, p2_choice)


import random

def first_player():
#This function will randomly decide who will go first;
	return random.choice((0, 1))


def display_board(board):
    print(" {} | {} | {} ".format(board[7],board[8],board[9]))
    print("-----------")
    print(" {} | {} | {} ".format(board[4],board[5],board[6]))
    print("-----------")
    print(" {} | {} | {} ".format(board[1],board[2],board[3]))


def player_choice(board, name, choice):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'\n{name} ({choice}), Choose your next position: (1-9) \t'))
        
        if position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position) or "": 
            #To check whether the given position is in the set [1-9] or whether it is empty or occupied;
            print(f"INVALID INPUT. This Position {position} is OCCUPIED. Please Try Again!\n")   
            
    return position


def space_check(board, position):
    #To check whether the given position is empty or occupied;
    return board[position] == ' '


def place_marker(board, choice, position):
    #To mark/replace the position on the board list;
    board[position] = choice


def full_board_check(board):
    #To check if the board is full, then the game is a draw;
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def win_check(board, choice):
    #To check if one of the following patterns are true; then the respective player has won!;
    
    #HORIZONTAL CHECK;
    return ( 
       ( board[1] == choice and board[2] == choice and board[3] == choice )
    or ( board[4] == choice and board[5] == choice and board[6] == choice )
    or ( board[7] == choice and board[8] == choice and board[9] == choice )
    #VERTICAL CHECK;
    or ( board[1] == choice and board[4] == choice and board[7] == choice )
    or ( board[2] == choice and board[5] == choice and board[8] == choice )
    or ( board[3] == choice and board[6] == choice and board[9] == choice )
    #DIAGONAL CHECK;
    or ( board[1] == choice and board[5] == choice and board[9] == choice )
    or ( board[3] == choice and board[5] == choice and board[7] == choice )  )



#def replay():
    #If the users want to play the game again?
#    replay = input("\nDo you want to play again? Enter Yes or No?\t")[0].upper()
#    return replay == 'Y'

###BETTER IMPLEMENTATION;
def replay():
    #If the users want to play the game again?
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



#MAIN PROGRAM STARTS;

print("\n\t\t NAMASTE! \n")
input("Press ENTER to start!")

default()
rules()

while True:
    ###########################################################################
    
    #Creating the board as a list; to be kept replacing it with user input;
    theBoard = [' ']*10

    #Printing choices;
    p1_name, p2_name = names()
    p1_choice, p2_choice = choice()
    print(f"\n{p1_name}:", p1_choice)
    print(f"{p2_name}:", p2_choice)
    
    #Printing randomly who will go first;
    rando = first_player()
    if rando == 0:
        turn = p1_name
    else:
        turn = p2_name
    print(f"\n{turn} will go first!")
    
    #Asking the user, if ready to play thee game; Output will be True or False;
    play_game = play()    
    
    while play_game:
        
        ############################
        #PLAYER1
        if turn == p1_name:
            
            #Displaying the board;
            display_board(theBoard)

            #Position of the input;
            position = player_choice(theBoard, p1_name, p1_choice)
            
            #Replacing the ' ' at *position* to *p1_choice* in *theBoard* list; 
            place_marker(theBoard, p1_choice, position)
            
            #To check if Player 1 has won after the current input;
            if win_check(theBoard, p1_choice):
                display_board(theBoard)
                print(f'\n\nCONGRATULATIONS {p1_name}! YOU HAVE WON THE GAME!')
                play_game = False
                
            else:
                #To check if the board is full; if yes, the game is a draw;
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('\n\nThe game is a DRAW!')
                    break
                #If none of the above is possible, next turn of Player 2;    
                else:
                    turn = p2_name
                    
                    
        ############################
        #PLAYER2            
        elif turn == p2_name:
            
            #Displaying the board;
            display_board(theBoard)

            #Position of the input;
            position = player_choice(theBoard, p2_name, p2_choice)
            
            #Replacing the ' ' at *position* to *p2_choice* in *theBoard* list; 
            place_marker(theBoard, p2_choice, position)
            
            #To check if Player 2 has won after the current input;
            if win_check(theBoard, p2_choice):
                display_board(theBoard)
                print(f'\n\nCONGRATULATIONS {p2_name}! YOU HAVE WON THE GAME!')
                play_game = False
                
            else:
                #To check if the board is full; if yes, the game is a draw;
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('\n\nThe game is a DRAW!')
                    break
                #If none of the above is possible, next turn of Player 2;       
                else:
                    turn = p1_name
                    
    #If the users want to play the game again?                
    if replay():
        #if Yes;
        continue
    else:
        #if No;
        break

    #########################################################################
    
print("\n\n\t\t\tTHE END!")


#END    