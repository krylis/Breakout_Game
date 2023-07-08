from turtle import Turtle


class Brick(Turtle):

    def __init__(self, color, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=2.5)
        self.color(color)
        self.penup()
        self.goto(position)
