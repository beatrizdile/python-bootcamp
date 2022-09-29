from turtle import Turtle

FONT = ("Courier", 8, "normal")


class StateName(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_the_state(self, s_name, x, y):
        self.goto(x, y)
        self.write(f"{s_name}", font=FONT)


