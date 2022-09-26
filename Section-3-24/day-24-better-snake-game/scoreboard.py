from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.goto(0, 270)
        self.points = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.points} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def new_point(self):
        self.points += 1
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as score:
                score.write(f"{self.points}")
        self.points = 0
        self.update_score()


