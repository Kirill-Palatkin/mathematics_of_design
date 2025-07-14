import turtle
import random


colors = ["#6495ED", "#11C7D4", "#E8E94E", "#070D8D", "#ad3aa2", "#6A5ACD", "#F67613", "#7B001C", "#FBD5BC",
          "#2EF812", "#2C4828", "#794020"]

window = turtle.Screen()
window.bgcolor("white")

snowflake = turtle.Turtle()
snowflake.color(random.choice(colors))
snowflake.speed(0)
snowflake.pensize(3)


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)


def draw_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


snowflake.penup()
snowflake.goto(-200, 100)
snowflake.pendown()

draw_snowflake(snowflake, 4, 400)

snowflake.hideturtle()

turtle.done()
