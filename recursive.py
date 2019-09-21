def factorial(x):
    print(x)
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)
        
y = int(input("what number do you want?"))
print(factorial(y))

