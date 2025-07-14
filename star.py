import turtle
import random

colors = ["#6495ED", "#11C7D4", "#E8E94E", "#070D8D", "#ad3aa2", "#6A5ACD", "#F67613", "#7B001C", "#FBD5BC",
          "#2EF812", "#2C4828", "#794020"]

star = turtle.Turtle()

star.speed(7)
star.pensize(4)

size = 400

star.penup()
star.goto(-200, 100)
star.pendown()

star.fillcolor(random.choice(colors))

star.begin_fill()

for _ in range(5):
    star.forward(size)
    star.right(144)

star.end_fill()

star.fillcolor(random.choice(colors))

star.begin_fill()
star.forward(size/2.63)
star.right(108)
star.forward(size/4.18)
star.left(74)
star.forward(size/4.15)
star.left(71)
star.forward(size/4.3)
star.left(72)
star.forward(size/4.3)
star.left(71)
star.forward(size/4.3)
star.end_fill()

star.hideturtle()

turtle.done()
