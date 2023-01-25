import turtle
#basic graphics
#beginners
#other one is pygame but is more complicated
import winsound #windows specific
#lets the code interact with the operating system with simple commands

wn = turtle.Screen()
#wn = window
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) 
#speedups the game, stops the window from updating, requires manual updating

#Score
score_a = 0
score_b = 0

#Paddle A

paddle_a = turtle.Turtle() 
#module_name.class_name()
paddle_a.speed(0) 
#speed of animation, necessary for turtle, sets it to max. possible speed
paddle_a.shape("square") 
#20 pxs by 20 pxs
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
#100 pxs tall, stretches the object
paddle_a.penup() 
#turtle draws line while moving by default this is to counter that
paddle_a.goto(-350,0) 
#position on the game console

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
#right side of the game console

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.09
ball.dy = 0.09
#random no. to try and test acc. to PC speed
#everytime the ball moves, it moves by specified pxs

#Pen

#pen object of the turtle writes something 
#in this case, the code will make it write the score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
#every turtle action starts at the middle of the screen and we move it
#without the penup() method it would draw lines while moving
pen.hideturtle()
pen.goto(0,260)
#score positioning on top
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
#default score

#Function

def paddle_a_up():
    y = paddle_a.ycor() 
    #the ycor method is from the turtle module and returns the y co-ordinate
    y += 20
    #adds 20 pxs to the y co-ordinate
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() 
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() 
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 20
    paddle_b.sety(y)

#Keyboard binding

wn.listen()
#tells the console to "listen" for keyboard i/p
wn.onkeypress(paddle_a_up, "w")
#when the user presses the lowercase w, the paddle_a_up func gets called
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
#Up for up arrow
wn.onkeypress(paddle_b_down, "Down")

#Main game loop

while True:
    wn.update() #updates the screen when the loop runs

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    #from the loop it moves everytime it runs
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    #compare ball's y co-ordinate and make it bounce once it gets to a certain pt.
    #screen is 800x600 ie. split into width=400 and height=300
    #ball itself is 20x20

    if ball.ycor() > 290:
        ball.sety(290)
        #resets the value so it doesn't go off-screen
        ball.dy *= -1
        #reverses the direction
            
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
    #check by setting initial ball direction to -ve, ball.dy = -0.09

    if ball.xcor() > 380:
        ball.goto(0,0)
        #game lost, paddle failed to intercept ball
        ball.dx *= -1
        score_a += 1
        pen.clear()
        #clears the previous printed value
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collisions

    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        #paddle b's x co-ordinate is 350 and is 20 pxs wide hence, left side of paddle b on x-axis will be at 340 _change acc. to o/p
        #if ball's y cor is below the top most part of the paddle and also above the bottom part, it should bounce
        #the paddle is 100 pxs tall and and it's center will be its y cor
        ball.setx(330)
        #there will be a glitch if you just miss the ball since the xcor will be >330 so there's one more condition to be added
        #ball.setx to 330 is to ensure that it doesn't slide along the paddle
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #snd_async is to ensure that the code doesn't stop functioning while the sound plays
    
    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    