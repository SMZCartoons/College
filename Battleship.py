player1 = "1 or 2"
player2 = "2 or 1"
Board = [["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"]]
def Battle (b):
    for i in range(0,len(b)):
        for j in range(0,len(b[i])):
            print(" " + b[i][j] + " ",end="")
        print(" ") 
Battle(Board) 
run = True
playernum = 1
while(True):
        print("You can position five ships: Carrier(5 spaces), Battleship(4 spaces), Cruiser(3 spaces), Submarine(3 spaces), and Destroyer(2 spaces)")
        pieces = input("What piece do you want to pick?")
        if(pieces == "Carrier"):
            column = int(input("Which column do you want it in?") )
            row = int(input("Which row do you want it in?"))
            Board[row][column] = "*"
            Board[row][column+1] = "*"
            Board[row][column+2] = "*"
            Board[row][column+3] = "*"
            Board[row][column+4] = "*"
        Battle(Board)
        if(pieces == "Battleship"):
            column = int(input("Which column do you want it in?") )
            row = int(input("Which row do you want it in?"))
            Board[row][column] = "*"
            Board[row][column+1] = "*"
            Board[row][column+2] = "*"
            Board[row][column+3] = "*"
        Battle(Board)
        if(pieces == "Cruiser"):
            column = int(input("Which column do you want it in?") )
            row = int(input("Which row do you want it in?"))
            Board[row][column] = "*"
            Board[row][column+1] = "*"
            Board[row][column+2] = "*"
        Battle(Board)
        if(pieces == "Submarine"):
            column = int(input("Which column do you want it in?") )
            row = int(input("Which row do you want it in?"))
            Board[row][column] = "*"
            Board[row][column+1] = "*"
            Board[row][column+2] = "*"
        Battle(Board)
        if(pieces == "Cruiser"):
            column = int(input("Which column do you want it in?") )
            row = int(input("Which row do you want it in?"))
            Board[row][column] = "*"
            Board[row][column+1] = "*"
        Battle(Board)
        
        if(playernum == 1):
            playernum = 2
        else:
            playernum=1
            print("Game over!")
while(run):
    first_collumn = input("Player "+str(playernum)+":Which Column would you like to move to?")
    ind = eval(first_collumn)
    for check in range(9,0):
        if(Board[check][ind] is "_"):
                if(playernum == 2):
                    Board[check][ind] = "1"
                    break
                if(playernum == 1):
                    Board[check][ind] = "2"
                    break
    Battle(Board)
for r in range(0,len(Board)):
    for c in range(0,len(Board[r])):
        if(c+3<len(Board[r])):
            if(Board[r][c] != "_" and Board[r][c] == Board[r][c+1] and Board[r][c] == Board[r][c+2] and Board[r][c] == Board[r][c+3]):
                print(Board[r][c]+" wins!")
                run=False
            if(r+3<len(Board)):
                if(Board[r][c] != "_" and Board[r][c] == Board[r+1][c] and Board[r][c] == Board[r+2][c] and Board[r][c] == Board[r+3][c]):
                    run=False
                    print(Board[r][c]+" wins!")
            if(c-3<len(Board[r]) and r+3<len(Board)):
                if(Board[r][c] != "_" and Board[r][c] == Board[r+1][c-1] and Board[r][c] == Board[r+2][r-2] and Board[r][c] == Board[r+3][r-3]):
                    run=False
                    print(Board[r][c]+" wins!")
            if(c+3<len(Board[r]) and r+3<len(Board)):
                if(Board[r][c] != "_" and Board[r][c] == Board[r+1][c+1] and Board[r][c] == Board[r+2][r+2] and Board[r][c] == Board[r+3][c+3]):
                    run=False
                    print(Board[r][c]+"wins!")