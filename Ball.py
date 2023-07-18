from turtle import Turtle
class Ball(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.movement_y = 10 
        self.movement_x = 10
        self.movespeed = 0.1
        self.penup()
        self.goto(position)
    
    def move(self):
        new_x = self.xcor() + self.movement_x
        new_y = self.ycor() + self.movement_y
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.movement_y *= -1 

    def bounce_x(self):
        self.movement_x *= -1
        self.movespeed *= 0.9

    def go_to_origin(self):
        self.movespeed = 0
        self.goto(0,0)
        
        



