import random
from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager, LANES_TWO
from scoreboard import Scoreboard, move_wave, LIST_OF_CARS, wave


screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
player.spawn(time)


screen.listen()
screen.onkey(key="Up", fun=player.go_up)
screen.onkey(key="Down", fun=player.go_down)

game_is_on = True
while game_is_on:
    if game_is_on:

        wave(CarManager, LANES_TWO, 3)

        while scoreboard.lv < 3 and game_is_on:
            move_wave(LIST_OF_CARS)
            first = LIST_OF_CARS[0]
            time.sleep(0.1)
            screen.update()

            if first.xcor() < 100:
                wave(CarManager, LANES_TWO, 3)

            move_wave(LIST_OF_CARS)

            for car in LIST_OF_CARS:
                if car.distance(player) < 25:
                    scoreboard.game_over()
                    game_is_on = False

            if player.ycor() > 280:
                scoreboard.lv_up()
                player.spawn(time)

            if len(LIST_OF_CARS) > 60:
                for i in range(-1, -5, -1):
                    LIST_OF_CARS.pop(i)

        if scoreboard.lv == 3:
            scoreboard.show_lv_up(time)

        while scoreboard.lv < 5 and game_is_on:

            time.sleep(0.08)
            screen.update()
            move_wave(LIST_OF_CARS)
            first = LIST_OF_CARS[0]

            if first.xcor() < 200:
                wave(CarManager, LANES_TWO, 3)

            move_wave(LIST_OF_CARS)

            for car in LIST_OF_CARS:
                if car.distance(player) < 27:
                    scoreboard.game_over()
                    game_is_on = False

            if player.ycor() > 280:
                scoreboard.lv_up()
                player.spawn(time)

            if len(LIST_OF_CARS) > 60:
                for i in range(-1, -5, -1):
                    LIST_OF_CARS.pop(i)

        if scoreboard.lv == 5:
            scoreboard.show_lv_up(time)

        while scoreboard.lv < 6 and game_is_on:

            time.sleep(0.08)
            screen.update()
            move_wave(LIST_OF_CARS)
            first = LIST_OF_CARS[0]

            if first.xcor() < 230:
                wave(CarManager, LANES_TWO, 3)

            move_wave(LIST_OF_CARS)

            for car in LIST_OF_CARS:
                if car.distance(player) < 27:
                    scoreboard.game_over()
                    game_is_on = False

            if player.ycor() > 280:
                scoreboard.lv_up()
                player.spawn(time)

            if len(LIST_OF_CARS) > 60:
                for i in range(-1, -5, -1):
                    LIST_OF_CARS.pop(i)

        if scoreboard.lv == 6:
            scoreboard.you_win()

screen.exitonclick()
