'''
for square in range(0,5):
    for square in range(0,5):
        print("*")
'''

choice = eval(input("how big do you want the square?"))
for square in range(0,choice):
    for square in range(0,choice):
        print("* ",end="")
    print("")