from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
import time

# set up screen
screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title("Breakout")
screen.tracer(0)

# create paddle and ball
paddle = Paddle()
ball = Ball()

# create row of bricks for each color and store them in the array
bricks = []
colors = ["red", "blue", "green"]
y_pos = 0
for color in colors:
    x_pos = -320
    for i in range(0, 8):
        bricks.append(Brick(color, (x_pos, y_pos)))
        x_pos += 90
    y_pos += 60

# make paddle move right or left when right or left arrow key is pressed
screen.listen()
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    # detect ball collision with side-wall and change ball's direction of movement
    if ball.xcor() >= 380 or ball.xcor() <= -390:
        ball.side_bounce()
    # detect collision with ceiling and change direction
    if ball.ycor() >= 290:
        ball.bounce()
    # detect collision with paddle and change ball's direction depending on what part of paddle ball collides with
    if ball.distance(paddle) <= 100 and ball.ycor() <= - 245:
        ball.bounce()
        if ball.xcor() < paddle.xcor():
            ball.bounce_left()
        else:
            ball.bounce_right()
    # detect collision with brick and change direction depending on what part of the brick the ball hit and delete brick
    for brick in bricks:
        if ball.distance(brick) <= 50 and (ball.ycor() <= brick.ycor() + 3 or ball.ycor() >= brick.ycor() - 3):
            ball.bounce()
            if ball.xcor() < brick.xcor():
                ball.bounce_left()
            else:
                ball.bounce_right()
            brick.reset()

screen.exitonclick()
