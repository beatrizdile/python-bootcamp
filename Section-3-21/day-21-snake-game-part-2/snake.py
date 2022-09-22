from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 5
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
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.my_turtles.append(turtle)

    def extend(self):
        # We can add the new turtle to the same position as the last turtle because the next coordinates the new turtle
        # will move to are the same as the current coordinates, while the last turtle will keep moving
        last = self.my_turtles[-1].position()
        self.add_segment(last)

    def move(self):
        for seg_num in range(len(self.my_turtles) - 1, 0, -1):
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
