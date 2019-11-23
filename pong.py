import turtle
# turtle opens a new window in order to organize the graphics

#SETUP
    
window = turtle.Screen()
#opens up the window in the first place (window can be written also as wn)
window.title("Pong For 2")
#is the title for the window opened
window.bgcolor("Beige")
#makes the background color
window.setup(width=900, height=700)
#sets up the size of the window (width and height)
window.tracer(0)
#??????

#PADDLE LEFT

paddle_left = turtle.Turtle()
#turtle.Turtle creates a new object on the screen
paddle_left.speed(0)
#makes the animation speed.  For now it is a rectangle
paddle_left.shape("turtle")
#makes the basic shape of the object
paddle_left.color("dark green")
#sets the color of the paddle
paddle_left.shapesize(stretch_wid=4.5, stretch_len=4.5)
#sets the width and length of the paddle
paddle_left.penup()
#takes off the line from the paddle, or any other unnecessary things
paddle_left.goto(-380,0)
#tells paddle where to go to

#PADDLE RIGHT

paddle_right = turtle.Turtle()
#turtle.Turtle creates a new object on the screen
paddle_right.speed(0)
#makes the animation speed.  For now it is a rectangle
paddle_right.shape("turtle")
#makes the basic shape of the object
paddle_right.color("red")
#sets the color of the paddle
paddle_right.shapesize(stretch_wid=4.5, stretch_len=4.5)
#sets the width and length of the paddle
paddle_right.penup()
#takes off the line from the paddle, or any other unnecessary things
paddle_right.goto(380,0)
#tells paddle where to go to
paddle_right.lt(180)
#rotates the paddle

#BALL

ball = turtle.Turtle()
#turtle.Turtle creates a new object on the screen
ball.speed(0)
#makes the animation speed.  For now it is a rectangle
ball.shape("triangle")
#makes the basic shape of the object
ball.color("brown")
#sets the color of the paddle
ball.shapesize(stretch_wid=2, stretch_len=2)
#sets the width and length of the paddle
ball.penup()
#takes off the line from the paddle, or any other unnecessary things
ball.goto(0,0)
#tells paddle where to go to

#FUNCTIONS

def paddle_left_up():
#every time you type this, it will do the following automatically
    y=paddle_left.ycor()
    #puts the position for y coordinate, and saves it into the variable y
    y += 70
    #is y = y+20 (20 means how much you want it to move up the screen)
    paddle_left.sety(y)
    #setting position of y to the new position
def paddle_left_down():
    y=paddle_left.ycor()
    y -= 70
    paddle_left.sety(y)
    
def paddle_right_up():
    y=paddle_right.ycor()
    y+=70
    paddle_right.sety(y)
def paddle_right_down():
    y=paddle_right.ycor()
    y-=70
    paddle_right.sety(y)
    
#KEYBOARD BINDING

window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")
window.listen()
#sets the keyboard keys to move paddles

#BALL MOVING

    

  
#RUN

while True:
    window.update()
    #updating the picture on the window (repaints itself)
    