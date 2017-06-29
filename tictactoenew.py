pieces = [["x","o","x"],["o","x","o"],["x","o","x"]]
for outerloop in range(0,3):
    print("")
    for innerloop in range(0,3):
        print("___ ",end="")
    print(pieces[outerloop])
