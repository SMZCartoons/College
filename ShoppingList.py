shoppinglist = []
while(True):
    choice = input("what items would you like to add?")
    if(choice != "none"):
        shoppinglist.append(choice)
        print(shoppinglist)
    if(choice == "none"):
        break

while(True):
    choice = input("what items would you like to remove?")
    if(choice != "none"):
        shoppinglist.remove(choice)
        print(shoppinglist)
    else:
        break
        
choice = input("Would you like to add, change, remove, or see the list?")
if(choice == "add"):
    while(True):
        choice = input("what items would you like to add?")
        if(choice != "none"):
            shoppinglist.append(choice)
            print(shoppinglist)
        if(choice == "none"):
            break
        
if(choice == "change"):
    while(True):
        if(choice != "none"):
            item = input("What item would you like to change?")
            newitem = input("what new item would you like to put in?")
            shoppinglist[item] = choice           
            print(shoppinglist)
        else:
            break
    
if(choice == "remove"):
    while(True):
        choice = input("what items would you like to remove?")
        if(choice != "none"):
            shoppinglist.remove(choice)
        else:
            break
        print(shoppinglist)
        
if(choice == "see the list"):
    print(shoppinglist)
    
    
    
