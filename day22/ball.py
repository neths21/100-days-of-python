from turtle import Turtle
WIDTH=1
HEIGHT=1
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(WIDTH,HEIGHT)
        self.penup()
        self.x_move=10
        self.y_move=10
    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)
    def bounce_y(self):
        self.y_move*=-1
    def bounce_x(self):
        self.x_move*=-1
    def reset_position(self):
        self.teleport(0,0)
        self.bounce_x()