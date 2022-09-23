from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.move_x = 2
        self.move_y = 2
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= - 1
        self.move_speed *= 0.5

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()


