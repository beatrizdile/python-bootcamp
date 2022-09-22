from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.points = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.points}", align=ALIGNMENT, font=FONT)

    def new_point(self):
        self.clear()
        self.points += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write("Game Over", align=ALIGNMENT, font=FONT)


