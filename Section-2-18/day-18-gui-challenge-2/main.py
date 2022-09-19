from turtle import Turtle, Screen
from random import choice


tim = Turtle()
colours = ["black", "cyan", "red", "green", "saddle brown", "indigo", "teal", "dark goldenrod"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.right(90)
tim.speed("fastest")


def random_walk(direction, color):
    tim.color(color)
    tim.setheading(direction)
    tim.forward(30)


for _ in range(100):
    random_walk(choice(directions), choice(colours))


screen = Screen()
screen.exitonclick()
