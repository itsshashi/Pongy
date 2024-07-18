from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.X_step=10
        self.Y_step=10
        self.fast=0.1

    def move(self):
        new_x=self.xcor()+self.X_step
        new_y=self.ycor()+self.Y_step
        self.goto(new_x,new_y)
    def bounce(self):
        self.Y_step*=-1


    def pad_bounce(self):
        self.X_step *=-1
    def refresh(self):
        self.goto(0,0)
        self.pad_bounce()
        self.fast=0.1
    def increase_speed(self):
        self.fast*=0.9