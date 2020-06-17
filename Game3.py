#!/usr/bin/python2.7
"""Blank Python 2.7 file"""
teeth = input("What is your name, M'seur?")
print("you," + teeth + ",are at the grocery store, but your list is messed up. Each word rhymes with something you would put on a Grocery store list. The only way to know what you want to buy is by deciphering it. Think carefully, and Good luck!")
Questions = ["Silk", "Peggs", "Yoda", "Chapel","Graham", "Scrape", "Price Beam", "Lake"]
Answers = ["Milk", "Eggs", "Soda", "Apple", "Ham", "Grape", "Ice Cream", "Cake"]
score = 0

while(True):
  y = input("rhymes with " + Questions[0])
  if(y == Answers[0]):
    print("Correct!")
    score = score+1
    print(score)
    del Questions[0]
    del Answers[0]
    print(y)
    if(len(Questions) == 0):
      break
  else:
    print("wrong")
    score = score-1
    print(score)
    print(y)
  if(Questions == []):
    if(Answers == []):
      print("Game over!")
      print(teeth + " got a score of " + score)
      print("Please email the score to sarvesh.sundaram@greenwichschools.org")
      break