from turtle import Turtle, Screen


tim = Turtle()
colours = ["black", "cyan", "red", "dark green", "saddle brown", "indigo", "teal", "dark goldenrod"]
tim.penup()
tim.left(90)
tim.forward(130)
tim.left(90)
tim.forward(60)
tim.right(180)
tim.pendown()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    i = shape_side_n - 3
    tim.color(colours[i])
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
