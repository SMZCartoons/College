player1 = "X or O"
player2 =  "O or X "
#pieces = [["x","o","x"],["o","x","o"],["x","o","x"]]
'''for outerloop in range(0,3):
    print("")
    for innerloop in range(0,3):
        print("___ ",end="")'''
pieces = [["___","___","___"],["___","___","___"],["___","___","___"]]
print((pieces[0][0]),end="")
print((pieces[0][1]),end="")
print((pieces[0][2]),end="")
print()
print((pieces[1][0]),end="")
print((pieces[1][1]),end="")
print((pieces[1][2]),end="")
print()
print((pieces[2][0]),end="")
print((pieces[2][1]),end="")
print((pieces[2][2]),end="")
print()
piece_chosen = input("Player 1: X or O?")
if(piece_chosen == "X"):
    print("OK.  You are controlling pieces X")
    print("Player 2: You are controlling pieces O")
if(piece_chosen == "O"):
    print("OK.  You are controlling pieces O")
    print("Player 2: you are controlling pieces X")
first_move = input("Player 1: Where would you like to move first?")

