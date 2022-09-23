from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.update()
screen.onkey(key="Up", fun=r_paddle.pad_up)
screen.onkey(key="Down", fun=r_paddle.pad_down)
screen.onkey(key="w", fun=l_paddle.pad_up)
screen.onkey(key="s", fun=l_paddle.pad_down)


game_on = True

while game_on:
    time_to_sleep = ball.move_speed
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()


screen.exitonclick()
