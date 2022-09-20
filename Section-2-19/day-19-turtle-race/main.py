from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
coordinates = [-70, -40, -10, 20, 50, 80]
my_turtles = []

for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=coordinates[i])
    my_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in my_turtles:
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        i.forward(random.randint(0, 10))


screen.exitonclick()
