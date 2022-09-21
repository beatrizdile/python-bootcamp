from turtle import Turtle

POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.my_turtles = []
        self.create_snake()
        self.head = self.my_turtles[0]

    def create_snake(self):
        for position in POSITIONS:
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(position, 0)
            self.my_turtles.append(turtle)

    def move(self):
        for seg_num in range(len(self.my_turtles)-1, 0, -1):
            new_x = self.my_turtles[seg_num - 1].xcor()
            new_y = self.my_turtles[seg_num - 1].ycor()
            self.my_turtles[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

