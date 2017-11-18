player1 = "1 or 2"
player2 = "2 or 1"
Board = [["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_"]]
def Battle ():
        print((Board[0][0]),end=" ")
        print((Board[0][1]),end=" ")
        print((Board[0][2]),end=" ")
        print((Board[0][3]),end=" ")
        print((Board[0][4]),end=" ")
        print((Board[0][5]),end=" ")
        print((Board[0][6]),end=" ")
        print((Board[0][7]),end=" ")
        print((Board[0][8]),end=" ")
        print()
        print((Board[1][0]),end=" ")
        print((Board[1][1]),end=" ")
        print((Board[1][2]),end=" ")
        print((Board[1][3]),end=" ")
        print((Board[1][4]),end=" ")
        print((Board[1][5]),end=" ")
        print((Board[1][6]),end=" ")
        print((Board[1][7]),end=" ")
        print((Board[1][8]),end=" ")
        print()
        print((Board[2][0]),end=" ")
        print((Board[2][1]),end=" ")
        print((Board[2][2]),end=" ")
        print((Board[2][3]),end=" ")
        print((Board[2][4]),end=" ")
        print((Board[2][5]),end=" ")
        print((Board[2][6]),end=" ")
        print((Board[2][7]),end=" ")
        print((Board[2][8]),end=" ")
        print()
        print((Board[3][0]),end=" ")
        print((Board[3][1]),end=" ")
        print((Board[3][2]),end=" ")
        print((Board[3][3]),end=" ")
        print((Board[3][4]),end=" ")
        print((Board[3][5]),end=" ")
        print((Board[3][6]),end=" ")
        print((Board[3][7]),end=" ")
        print((Board[3][8]),end=" ")
        print()
        print((Board[4][0]),end=" ")
        print((Board[4][1]),end=" ")
        print((Board[4][2]),end=" ")
        print((Board[4][3]),end=" ")
        print((Board[4][4]),end=" ")
        print((Board[4][5]),end=" ")
        print((Board[4][6]),end=" ")
        print((Board[4][7]),end=" ")
        print((Board[4][8]),end=" ")
        print()
        print((Board[5][0]),end=" ")
        print((Board[5][1]),end=" ")
        print((Board[5][2]),end=" ")
        print((Board[5][3]),end=" ")
        print((Board[5][4]),end=" ")
        print((Board[5][5]),end=" ")
        print((Board[5][6]),end=" ")
        print((Board[5][7]),end=" ")
        print((Board[5][8]),end=" ")
        print()
        print((Board[6][0]),end=" ")
        print((Board[6][1]),end=" ")
        print((Board[6][2]),end=" ")
        print((Board[6][3]),end=" ")
        print((Board[6][4]),end=" ")
        print((Board[6][5]),end=" ")
        print((Board[6][6]),end=" ")
        print((Board[6][7]),end=" ")
        print((Board[6][8]),end=" ")
        print()
        print((Board[7][0]),end=" ")
        print((Board[7][1]),end=" ")
        print((Board[7][2]),end=" ")
        print((Board[7][3]),end=" ")
        print((Board[7][4]),end=" ")
        print((Board[7][5]),end=" ")
        print((Board[7][6]),end=" ")
        print((Board[7][7]),end=" ")
        print((Board[7][8]),end=" ")
        print()
        print((Board[8][0]),end=" ")
        print((Board[8][1]),end=" ")
        print((Board[8][2]),end=" ")
        print((Board[8][3]),end=" ")
        print((Board[8][4]),end=" ")
        print((Board[8][5]),end=" ")
        print((Board[8][6]),end=" ")
        print((Board[8][7]),end=" ")
        print((Board[8][8]),end=" ")
        print()
Battle() 
run = True
playernum = 1
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
    for row in Board:
        print (Board,end=" ")
    print()
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
        if(playernum == 1):
            playernum = 2
        else:
            playernum=1
            print("Game over!")