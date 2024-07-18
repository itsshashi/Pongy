from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import  Scoreboard
import time
wall=Turtle()
screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title("PONG GAME")
box=Paddle(350,0)
user=Paddle(-350,0)
ball=Ball()

screen.listen()
screen.onkey(box.up,'Up')
screen.onkey(box.down,'Down')
screen.onkey(user.up,"w")
screen.onkey(user.down,'s')
score = Scoreboard()
score.update_score()
is_on=True
while is_on:
    time.sleep(ball.fast)

    screen.update()
    ball.move()

#detect the collision on surface
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    #detect collision with paddle
    if ball.xcor()>320 and ball.distance(box)<80 or ball.distance(user)<80 and ball.xcor()<-320:
        ball.pad_bounce()
        ball.increase_speed()



    #ball passed the defined width then it pass through it and new ball is refreshed

    if ball.xcor()>380:
        score.left_score()
        ball.refresh()


    if ball.xcor()<-380:
        score.right_score()
        ball.refresh()





    #increase score of opposite when ball passes through opposite territory









screen.exitonclick()