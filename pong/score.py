from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.box_score=0
        self.user_score=0


    def update_score(self):
        self.goto(-100,200)
        self.write(self.box_score,align='center',font=("Courier",40,"bold"))
        self.goto(100,200)
        self.write(self.user_score,align='center',font=('Courier',40,'bold'))

    def left_score(self):
        self.box_score+=1
        self.clear()
        self.update_score()
    def right_score(self):
        self.user_score+=1
        self.clear()
        self.update_score()