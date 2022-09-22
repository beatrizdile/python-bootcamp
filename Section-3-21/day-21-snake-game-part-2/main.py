from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
positions = [0, -20, -40]
my_turtles = []
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Score()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.new_point()
        snake.extend()


    #Detec collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail (excluding head)
    for seg in snake.my_turtles[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
