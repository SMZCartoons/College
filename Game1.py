#!/usr/bin/python2.7
"""Blank Python 2.7 file"""
teach = input("what is your name?")
if(teach == "Joe"):
  who = input("Who's Joe?")
  if(who == "Joe Mama"):
    print("darn you. ")
print("This is a focus game. You are professor " + teach + " , and you are grading papers. Find the mistake in each sentence (IF ANY), and enter it in. If there is no mistake, enter the original sentence. Good luck!")
prompts = ["Do you wenna build an snowman?", "1+1 = 1", "My earaser is worser.", "1 x 1 = 2", "This is a sentence", "I love my mother!", "I going to store now", "3 x3 = 6", "2 x 5 = 10", "The Beatles are my favorite band dude?", "After I sated down I wanted to eating.", "1+5 = 6", "the aphebet is complicated?"]
answers = ["Do you wanna build a snowman?", "1+1 = 2", "My eraser is worse.", "1 x 1 = 1", "This is a sentence.", "I love my mother!", "I am going to the store now.", "3 x 3 = 9", "2 x 5 = 10", "The Beatles are my favorite band, dude!", "After I sat down, I wanted to eat", "1+5 = 6", "The alphabet is complicated!"]
score = 0
while(True):
  question = input(prompts[0])
  if(question == answers[0]):
    print("good job!")
    score = score+1
    print(score)
    del prompts[0]
    del answers[0]
  else:
    print("try again")
    score = score-1
    print(score)
    print(question)
  if prompts == []:
    if answers == []:
      print("Game over!")
      print(teach+ " got a score of " +score)
      print("Please email the score to sarvesh.sundaram@greenwichschools.org")
      break

