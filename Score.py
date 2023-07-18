from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0 
        self.score2 = 0
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(0,240)

    def update_scoreboard(self):
        self.write(f"{self.score1}|{self.score2}",align="center", font=("white",40,"normal"))
    
    def earn_point_1(self):
        self.score1 += 1
        self.clear()
        self.update_scoreboard()

    def earn_point_2(self):
        self.score2 += 1
        self.clear()
        self.update_scoreboard()




