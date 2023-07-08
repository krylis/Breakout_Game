from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.005)
    ball.move()
    if ball.xcor() >= 390 or ball.xcor() <= -390:
        ball.side_bounce()
    if ball.ycor() >= 290:
        ball.bounce()
    if ball.distance(paddle) <= 100 and ball.ycor() <= - 245:
        ball.bounce()
        if ball.xcor() < paddle.xcor():
            ball.bounce_left()
        else:
            ball.bounce_right()


screen.exitonclick()
