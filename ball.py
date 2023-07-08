from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.goto(0, -100)

    def reset(self):
        self.goto(0, -100)
        self.x_move = 1
        self.y_move = 1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1

    def side_bounce(self):
        self.x_move *= -1

    def bounce_left(self):
        self.x_move = -1

    def bounce_right(self):
        self.x_move = 1
