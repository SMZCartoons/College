player1 = "A or 0"
player2 = "0 or A"
pieces = [["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"]]
for row in pieces:
    for piece in row:
        print (piece,end=" ")
    print()
print("INSTRUCTIONS:") 
print("This is a game of Connect Four.  Here you must enter your coordinates for where your pieces are.")  
print("For the column, it is column 0, 1, 2, 3, 4, 5, and 6.")  
print("So for instance, if I were to enter the first column, I would say Column 0")
print("Player 1 is controlling pieces A")
print("Player 2: You are controlling pieces O")
run = True
playernum = 1
while(run):
    first_move_collumn = input("Player "+str(playernum)+": Which column would you like to move to?")
    ind = eval(first_move_collumn)
    for check in range(6,0,-1):
        if(pieces[check][ind] is "_"):
            if(playernum == 2):
                pieces[check][ind] = "O"
                break
            if(playernum == 1):
                pieces[check][ind] = "A"
                break
    for row in pieces:
        for piece in row:
            print (piece,end=" ")
        print()
    for r in range(0,len(pieces)):
        for c in range(0,len(pieces[r])):
            if(c+3<len(pieces[r])):
                if(pieces[r][c] != "_" and pieces[r][c] == pieces[r][c+1] and pieces[r][c] == pieces[r][c+2] and pieces[r][c] == pieces[r][c+3]):
                    print(pieces[r][c]+" wins!")
                    run=False
            if(r+3<len(pieces)):
                if(pieces[r][c] != "_" and pieces[r][c] == pieces[r+1][c] and pieces[r][c] == pieces[r+2][c] and pieces[r][c] == pieces[r+3][c]):
                    run=False
                    print(pieces[r][c]+" wins!")
            if(c-3>=0 and r+3<len(pieces)):
                if(pieces[r][c] != "_" and pieces[r][c] == pieces[r+1][c-1] and pieces[r][c] == pieces[r+2][r-2] and pieces[r][c] == pieces[r+3][r-3]):
                    run=False
                    print(pieces[r][c]+" wins!")
            if(c+3<len(pieces[r]) and r+3<len(pieces)):
                if(pieces[r][c] != "_" and pieces[r][c] == pieces[r+1][c+1] and pieces[r][c] == pieces[r+2][r+2] and pieces[r][c] == pieces[r+3][c+3]):
                    run=False
                    print(pieces[r][c]+" wins!")
    if(playernum == 1):
        playernum = 2
    else:
        playernum = 1

print("Game over!")
    
    
