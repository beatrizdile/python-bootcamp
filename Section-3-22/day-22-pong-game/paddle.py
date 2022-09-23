from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def pad_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def pad_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

