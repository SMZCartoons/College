#!/usr/bin/python2.7
"""Blank Python 2.7 file"""

Books = ["Addition Quiz", "Comma Worksheet", "Essay on Huck Finn", "Subtraction Quiz", "George Washington's Life", "Curious George", "Chemistry Textbook", "Decimals and Fractions", "A Study of the Milky Way","How to type", "Computers and their uses", "The History of the World"]
Answers = ["Math folder", "English folder", "Reading folder", "Math folder", "History folder", "English folder", "Science folder", "Math folder", "Science folder", "Technology folder", "Technology folder", "History folder"]
teeth = input("what is your name, fair person?")
print("You, " + teeth + ", are a student who has a disorganized backpack! You have 2 minutes to organize all the papers before dinner! Sort them into either the Math folder, English folder, Science folder, Technology folder, or History folder. Good luck, and keep in mind that capitalization and spelling counts!!")
score = 0
while(True):
    question = input("Where does " + Books[0] + " go?")
    if(question == Answers[0]):
      print("Good job!")
      score = score+1
      print(score)
      del Books[0]
      del Answers[0]

    else:
      print("Try again!")
      print(question)
      score = score-1
      print(score)

    if(Answers == []):
      if(Books == []):
        print("Game over!")
        print(teeth + "got a score of" + score)
        print("Please email the score to sarvesh.sundaram@greenwichschools.org")
        break



