from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANES_TWO = []

for i in range(-235, 250, +30):
    LANES_TWO.append(i)


class CarManager(Turtle):
    def __init__(self, lanes):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.seth(180)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(280, lanes)
        self.movement = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.movement)

    def faster(self):
        self.movement += MOVE_INCREMENT


