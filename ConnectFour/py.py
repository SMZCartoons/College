player1 = "A or 0"
player2 = "0 or A"
pieces = [["___","___","___","___","___","___","___"],["___","___","___","___","___","___","___"],["___","___","___","___","___","___","___"],["___","___","___","___","___","___","___"],["___","___","___","___","___","___","___"],["___","___","___","___","___","___","___"],["___","___","___","___","___","___","___"]]
print((pieces[0][0]),end=" ")
print((pieces[0][1]),end=" ")
print((pieces[0][2]),end=" ")
print((pieces[0][3]),end=" ")
print((pieces[0][4]),end=" ")
print((pieces[0][5]),end=" ")
print((pieces[0][6]),end=" ")
print()
print((pieces[1][0]),end=" ")
print((pieces[1][1]),end=" ")
print((pieces[1][2]),end=" ")
print((pieces[1][3]),end=" ")
print((pieces[1][4]),end=" ")
print((pieces[1][5]),end=" ")
print((pieces[1][6]),end=" ")
print()
print((pieces[2][0]),end=" ")
print((pieces[2][1]),end=" ")
print((pieces[2][2]),end=" ")
print((pieces[2][3]),end=" ")
print((pieces[2][4]),end=" ")
print((pieces[2][5]),end=" ")
print((pieces[2][6]),end=" ")
print()
print((pieces[3][0]),end=" ")
print((pieces[3][1]),end=" ")
print((pieces[3][2]),end=" ")
print((pieces[3][3]),end=" ")
print((pieces[3][4]),end=" ")
print((pieces[3][5]),end=" ")
print((pieces[3][6]),end=" ")
print()
print((pieces[4][0]),end=" ")
print((pieces[4][1]),end=" ")
print((pieces[4][2]),end=" ")
print((pieces[4][3]),end=" ")
print((pieces[4][4]),end=" ")
print((pieces[4][5]),end=" ")
print((pieces[4][6]),end=" ")
print()
print((pieces[5][0]),end=" ")
print((pieces[5][1]),end=" ")
print((pieces[5][2]),end=" ")
print((pieces[5][3]),end=" ")
print((pieces[5][4]),end=" ")
print((pieces[5][5]),end=" ")
print((pieces[5][6]),end=" ")
print()
print((pieces[6][0]),end=" ")
print((pieces[6][1]),end=" ")
print((pieces[6][2]),end=" ")
print((pieces[6][3]),end=" ")
print((pieces[6][4]),end=" ")
print((pieces[6][5]),end=" ")
print((pieces[6][6]),end=" ")
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
    for check in range (6,0,-1):
        if(pieces[check][ind] is "___"):
            if(playernum == 2):
                pieces[check][ind] = " O "
                break
            if(playernum == 1):
                pieces[check][ind] = " A "
                break
    print((pieces[0][0]),end=" ")
    print((pieces[0][1]),end=" ")
    print((pieces[0][2]),end=" ")
    print((pieces[0][3]),end=" ")
    print((pieces[0][4]),end=" ")
    print((pieces[0][5]),end=" ")
    print((pieces[0][6]),end=" ")
    print()
    print((pieces[1][0]),end=" ")
    print((pieces[1][1]),end=" ")
    print((pieces[1][2]),end=" ")
    print((pieces[1][3]),end=" ")
    print((pieces[1][4]),end=" ")
    print((pieces[1][5]),end=" ")
    print((pieces[1][6]),end=" ")
    print()
    print((pieces[2][0]),end=" ")
    print((pieces[2][1]),end=" ")
    print((pieces[2][2]),end=" ")
    print((pieces[2][3]),end=" ")
    print((pieces[2][4]),end=" ")
    print((pieces[2][5]),end=" ")
    print((pieces[2][6]),end=" ")
    print()
    print((pieces[3][0]),end=" ")
    print((pieces[3][1]),end=" ")
    print((pieces[3][2]),end=" ")
    print((pieces[3][3]),end=" ")
    print((pieces[3][4]),end=" ")
    print((pieces[3][5]),end=" ")
    print((pieces[3][6]),end=" ")
    print()
    print((pieces[4][0]),end=" ")
    print((pieces[4][1]),end=" ")
    print((pieces[4][2]),end=" ")
    print((pieces[4][3]),end=" ")
    print((pieces[4][4]),end=" ")
    print((pieces[4][5]),end=" ")
    print((pieces[4][6]),end=" ")
    print()
    print((pieces[5][0]),end=" ")
    print((pieces[5][1]),end=" ")
    print((pieces[5][2]),end=" ")
    print((pieces[5][3]),end=" ")
    print((pieces[5][4]),end=" ")
    print((pieces[5][5]),end=" ")
    print((pieces[5][6]),end=" ")
    print()
    print((pieces[6][0]),end=" ")
    print((pieces[6][1]),end=" ")
    print((pieces[6][2]),end=" ")
    print((pieces[6][3]),end=" ")
    print((pieces[6][4]),end=" ")
    print((pieces[6][5]),end=" ")
    print((pieces[6][6]),end=" ")
    print()
    lastA = True
    Quantity = 0
    for row in pieces:
        for block in row:
            if(lastA == True and block == "A"):
                Quantity += 1
            elif(lastA == False and block == "O"):
                Quantity += 1
            else: 
                Quantity = 1
            if(Quantity == 4):
                print("Game Over!")
                run = False
    for block in pieces:
        for block in row:
            if(lastA == True and block == "A"):
                Quantity += 1
            elif(lastA == False and block == "O"):
                Quantity += 1
            else: 
                Quantity = 1
            if(Quantity == 4):
                print("Game Over!")
                run = False
    if(playernum == 1):
        playernum = 2
    else:
        playernum = 1       
    
    