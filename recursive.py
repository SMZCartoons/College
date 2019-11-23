def factorial(x):
    print(x)
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)
        
y = int(input("what number do you want?"))
print(factorial(y))

candy = ["reeces", "hersheys", "snickers"]

#method 1, saying with each item in candy, execute whatever you want w/ item as current candy

for item in candy:
    print(item)

#second method, assign candy to a for loop to find out how many items are in the list, and print each one individually
for item in range(len(candy)):
    print(candy[item])
#len = length of something

#method 2.5 - for loops
for candy in candy:
    print(" my teachers is named " + candy)



