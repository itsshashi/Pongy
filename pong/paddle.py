from turtle import Turtle
import time


class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color('white')
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x,y)
    def up(self):
        ney_y=self.ycor()+20
        self.goto(self.xcor(),ney_y)
    def down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)


