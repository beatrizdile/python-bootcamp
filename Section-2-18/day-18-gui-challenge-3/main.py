import turtle as t
import random


tim = t.Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.right(90)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_walk(direction, color):
    tim.color(color)
    tim.setheading(direction)
    tim.forward(30)


for _ in range(200):
    random_walk(random.choice(directions), (random_color()))


screen = t.Screen()
screen.exitonclick()
