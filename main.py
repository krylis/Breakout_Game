from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.paddle_right, "Right")
screen.onkey(paddle.paddle_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
