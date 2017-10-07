player1 = "X or O"
player2 =  "O or X "
#pieces = [["x","o","x"],["o","x","o"],["x","o","x"]]
'''for outerloop in range(0,3):
    print("")
    for innerloop in range(0,3):
        print("___ ",end="")'''
pieces = [["___","___","___"],["___","___","___"],["___","___","___"]]
print((pieces[0][0]),end=" ")
print((pieces[0][1]),end=" ")
print((pieces[0][2]),end=" ")
print()
print((pieces[1][0]),end=" ")
print((pieces[1][1]),end=" ")
print((pieces[1][2]),end=" ")
print()
print((pieces[2][0]),end=" ")
print((pieces[2][1]),end=" ")
print((pieces[2][2]),end=" ")
print()
print("INSTRUCTIONS:") 
print("This is a game of Tic-tac-Toe.  here you must enter your coordinates for where your pieces are.")  
print("The first row is row 0.  Second row is row 1, and so on.  For the column, it is column 0, 1, and 2.")  
print("So for instance, if I were to enter the first row and first column, I would say Row 0, Column 0")
print("OK.  You are controlling pieces X")
print("Player 2: You are controlling pieces O")
game_not_over = True
while(game_not_over):
    first_move_row = input("Player 1: Which row would you like to move to?")
    first_move_collumn = input("Player 1: Which column would you like to move to?")
    #if(first_move_row == "0"):
    #    if(first_move_collumn == "0"):
    
    pieces[eval(first_move_row)][eval(first_move_collumn)] = "X"
    
    print((pieces[0][0]),end=" ")
    print((pieces[0][1]),end=" ")
    print((pieces[0][2]),end=" ")
    print()
    print((pieces[1][0]),end=" ")
    print((pieces[1][1]),end=" ")
    print((pieces[1][2]),end=" ")
    print()
    print((pieces[2][0]),end=" ")
    print((pieces[2][1]),end=" ")
    print((pieces[2][2]),end=" ")
    print()
for piece in range (0,3):
    if(pieces[0][piece] == "O") and(pieces[1][piece] == "O") and(pieces[2][piece] == "O"):
        print("Game Over!")
        game_not_over = False
    if(pieces[piece][0] == "O") and(pieces[piece][1] == "O") and(pieces[piece][2] == "O"):
        print("Game Over!")
        game_not_over = False
    if(pieces[0][0] == "O" and pieces[1][1] == "O" and pieces[2][2] == "O") or(pieces[0][2] == "O" and pieces[1][1] == "O" and pieces[2][0] == "O"):
        print("Game Over!")
        game_not_over = False
        first_move_row = input("Player 2: Which row would you like to move to?")
        first_move_collumn = input("Player 2: Which column would you like to move to?")
        pieces[eval(first_move_row)][eval(first_move_collumn)] = "O"
    
    print((pieces[0][0]),end=" ")
    print((pieces[0][1]),end=" ")
    print((pieces[0][2]),end=" ")
    print()
    print((pieces[1][0]),end=" ")
    print((pieces[1][1]),end=" ")
    print((pieces[1][2]),end=" ")
    print()
    print((pieces[2][0]),end=" ")
    print((pieces[2][1]),end=" ")
    print((pieces[2][2]),end=" ")
for piece in range (0,3):
    if(pieces[0][piece] == "X") and(pieces[1][piece] == "X") and(pieces[2][piece] == "X"):
         print("Game Over!")
         game_not_over = False
    if(pieces[piece][0] == "X") and(pieces[piece][1] == "X") and(pieces[piece][2] == "X"):
        print("Game Over!")
        game_not_over = False
    if(pieces[0][0] == "X" and pieces[1][1] == "X" and pieces[2][2] == "X") or(pieces[0][2] == "X" and pieces[1][1] == "X" and pieces[2][0] == "X"):
    print("Game Over!")
    game_not_over = False
        
        
        