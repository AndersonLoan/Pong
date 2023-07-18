from turtle import Screen, Turtle,done
import turtle
from Paddle import Paddle
from Ball import Ball
from Score import ScoreBoard
import time 

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball((0,0))
score = ScoreBoard()
screen = Screen()

screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
#movements based on arrow keys

screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


game_on = True
score.update_scoreboard()

while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ((ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320) ):
        ball.bounce_x()

    if ball.xcor() > 380:
        score.earn_point_1()
        ball.go_to_origin()
    
    if ball.xcor() < -380:
        score.earn_point_2()
        ball.go_to_origin()
        
screen.exitonclick()


