choice = input("You Walk into a crossroads.  Do you go left or right?")
print(choice)
if(choice == "left"):
     print("You reach a dead end")
if(choice == "right"):
    print("You enter a chamber with an area of 50 square feet")
choice = input("You see a huge Gorilla blocking the exit.  Do you attack or run away?")
print(choice)
if(choice == "run away"):
    print("You run to the door, but the ape is faster.  It stomps on You.  You Die.")
    print("Game over")
if(choice == "attack"):
    print("You climb up the ape and reach its neck, and choke it.")
    choice = input("You see a treasure chest.  Do you open it, or exit the room?")
if(choice == "open it"):
    print("Acid sprays on your face and you die.  Game Over")
if(choice == "exit the room"):
    print("You reach a corridor and walk 50 feet and then reach another room.  A giant approaches you.")
    print("He says, 'answer this question, and you shall pass.")
    choice = input("True or False: Did Stan Lee created Captain America?")
    print(choice)
if(choice == "True"):
    print("Giant roars 'Wrong Answer!'  he smashes you, and you die.  Game over.")
if(choice == "False"):
    print("Giant nods his head, and moves aside.  he then offers you a sword.")
if(choice == "take it"):
    print("The giant gives it to you, and you exit in peace")
    

