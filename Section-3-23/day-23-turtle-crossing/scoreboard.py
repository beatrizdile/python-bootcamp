from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")
LIST_OF_CARS = []


def move_wave(list_of_cars):
    for car in list_of_cars:
        car.move()


def wave(fun, lanes, number_of_samples):
    random_cars = random.sample(lanes, number_of_samples)
    for a in random_cars:
        car = fun(a)
        LIST_OF_CARS.insert(0, car)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)
        self.lv = 0
        self.current_score()

    def current_score(self):
        self.write(f"Level: {self.lv}", align="center", font=FONT)
        self.goto(-210, 250)

    def lv_up(self):
        self.clear()
        self.lv = self.lv + 1
        self.current_score()

    def show_lv_up(self, time):
        self.home()
        self.write(f"Level Up", align="center", font=FONT)
        time.sleep(2)
        self.clear()
        self.goto(-210, 250)
        self.current_score()

    def game_over(self):
        self.home()
        self.write(f"Game Over", align="center", font=FONT)

    def you_win(self):
        self.home()
        self.write(f"Victory", align="center", font=FONT)