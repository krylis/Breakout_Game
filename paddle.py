from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=10, stretch_wid=0.5)
        self.penup()
        self.goto(0, -260)

    def go_right(self):
        self.goto(self.xcor() + 20, self.ycor())

    def go_left(self):
        self.goto(self.xcor() - 20, self.ycor())
