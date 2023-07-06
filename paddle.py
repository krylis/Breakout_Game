from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=8, stretch_wid=1)
        self.penup()
        self.goto(0, -260)

    def paddle_right(self):
        self.goto(self.xcor() + 20, self.ycor())

    def paddle_left(self):
        self.goto(self.xcor() - 20, self.ycor())
