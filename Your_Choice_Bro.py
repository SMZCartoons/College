while(True): 
    choice = input("You Walk into a crossroads.  Do you go left or right?")
    print(choice)
    if(choice == "left"):
        print("You reach a dead end.  Game Over!")
        #if(input("Do you want to play again?")=="yes"):
            
    elif(choice == "right"):
        print(" You enter a chamber with an area of 50 square feet")
        choice = input("You see a huge Gorilla blocking the exit.  Do you attack or run away?")
    print(choice)
    if(choice == "run away"):
        print("You run to the door, but the ape is faster.  It stomps on You.  You Die.")
        print("Game over")
    elif(choice == "attack"):
        print("You climb up the ape and reach its neck, and choke it.")
        choice = input("You see a treasure chest.  Do you open it, or exit the room?")
    if(choice == "open it"):
        print("Acid sprays on your face and you die.  Game Over")
    elif (choice == "exit the room"):
        print("You reach a corridor and walk 50 feet and then reach another room.  A giant approaches you.")
        print("He says, 'answer this question, and you shall pass.")
        choice = input("True or False: Did Stan Lee created Captain America?")
        print(choice)
    if(choice == "True"):
        print("Giant roars 'Wrong Answer!'  he smashes you, and you die.  Game over.")
    elif(choice == "False"):
        choice = input("Giant nods his head, and moves aside.  he then offers you a sword.  Do you take it or decline?")
        print("choice")
    if(choice == "decline"):
        print("Giant roars in outrage and guts you with the sword.  You die.  Game over.")
    elif(choice == "take it"):
        print("The giant gives it to you, and you exit in peace")
        choice = input("You reach another intersection.  Do you want to go to path 1 or path 2?")
    if(choice == "path 1"):
        print("You fall into a stone pit and die of thirst and starvation.  Game over.")
    elif(choice == "path 2"):
        choice = input("You go forward 50 feet, and then enter your final room.  In front of you is 3 giant snakes.  Do you attack or do you try to make peace?")
        print(choice)
    if(choice == "try to make peace"):
        print("The snakes don't understand English, so they eat you.  You die.  Game Over")
    elif(choice == "attack"):
        choice = input("The snakes 'fuse'into one huge snake, and use their bodies to trip you, and squeezes you.  Do you want to use your sword?")
        print(choice)
    if(choice == "yes"):
        print("You pull the sword, but it explodes and kills you.  The Giant, who seems to have been following you, laughs in glee, and scoops up your remains from the snake, and runs back to his room to make soup out of you.  ")
    elif(choice == "no"):
        print("You manage to wriggle free from the snake because their body keeps on touching the sword.  You now are free.")
        choice = input("Do you want to use your sword NOW?")
    if(choice == "no"):
        print("You have nothing to defend yourself.  The snakes kill you.  Game over")
    elif(choice == "yes"):
        print("You throw your sword at the snake, and as soon as it makes contact, it explodes, killing the snake.")
        print("The giant appears, howling in rage.  He yells that the sword was supposed to kill you, and now everything was ruined, and charges you.")
        choice = input("Do you Attack or Run away?")
    if(choice == "Attack"):
        print("The giant makes destroys you, and then eats you.  Game over.")
    elif(choice == "Run away"):
        print("you have speed, so you out run the giant, and run out of the exit, which is too small for the giant.")
        choice = input("you reach a 3-way crossing.  Do you go road 1, road 2, or road 3?")
    if(choice == "road 1"):
        print("You end up at school and learn boring things, and have 10 tests and quizzes.  Sorry!")
    elif(choice == "road 2"):
        print("you end up home and get sent to do chores because your parents think you skipped school.  Too bad!")
    elif(choice == "road 3"):
        print("You end up at Summer Tech and have a Blast!!!  Good Choice!")
        print("game over!") 
        break

    
    

    
    
    
    

