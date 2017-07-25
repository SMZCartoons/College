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
piece_chosen = input("Player 1: X or O?")
if(piece_chosen == "X"):
    print("OK.  You are controlling pieces X")
    print("Player 2: You are controlling pieces O")
if(piece_chosen == "O"):
    print("OK.  You are controlling pieces O")
    print("Player 2: you are controlling pieces X")

while(True):
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
    if(pieces[0][0] == "X" and pieces[0][1] == "X" and pieces[0][2] == "X"):
        print("Game Over!")
        break
    if(pieces[1][0] == "X" and pieces[1][1] == "X" and pieces[1][2] == "X"):
        print("Game Over!")
        break
    if(pieces[2][0] == "X" and pieces[2][1] == "X" and pieces[2][2] == "X"):
        print("Game Over!")
        break
    if(pieces[0][0] == "X" and pieces[1][1] == "X" and pieces[2][2] == "X"):
        print("Game Over!")
        break
    if(pieces[0][2] == "X" and pieces[1][1] == "X" and pieces[3][0] == "X"):
        print("Game Over!")
        break
    if(pieces[0][0] == "X" and pieces[1][0] == "X" and pieces[2][0] == "X"):
        print("Game Over!")
        break
    if(pieces[0][1] == "X" and pieces[1][1] == "X" and pieces[2][1] == "X"):
        print("Game Over!")
        break
    if(pieces[0][2] == "X" and pieces[1][2] == "X" and pieces[2][2] == "X"):
        print("Game Over!")
        break
    
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
    if(pieces[0][0] == "O" and pieces[0][1] == "O" and pieces[0][2] == "O"):
        print("Game Over!")
        break
    if(pieces[1][0] == "O" and pieces[1][1] == "O" and pieces[1][2] == "O"):
        print("Game Over!")
        break
    if(pieces[2][0] == "O" and pieces[2][1] == "O" and pieces[2][2] == "O"):
        print("Game Over!")
        break
    if(pieces[0][0] == "O" and pieces[1][1] == "O" and pieces[2][2] == "O"):
        print("Game Over!")
        break
    if(pieces[0][2] == "O" and pieces[1][1] == "O" and pieces[3][0] == "O"):
        print("Game Over!")
        break
    if(pieces[0][0] == "O" and pieces[1][0] == "O" and pieces[2][0] == "O"):
        print("Game Over!")
        break
    if(pieces[0][1] == "O" and pieces[1][1] == "O" and pieces[2][1] == "O"):
        print("Game Over!")
        break   
    if(pieces[0][2] == "O" and pieces[1][2] == "O" and pieces[2][2] == "O"):
        print("Game Over!")
        break