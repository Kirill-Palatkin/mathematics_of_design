import turtle
import random


def draw_branch(t, length):
    t.forward(length)
    t.backward(length)


def draw_snowflake(t, size, branches):
    angle = 360 / branches
    for _ in range(branches):
        t.forward(size)
        for _ in range(1):
            draw_branch(t, size // 3)
            t.right(45)
            draw_branch(t, size // 3)
            t.left(90)
            draw_branch(t, size // 3)
            t.right(45)
        t.backward(size)
        t.right(angle)


branches = int(input('Введите количество ветвей (четное число): '))
while branches % 2 != 0:
    print('Введено нечетное число.')
    branches = int(input('Введите количество ветвей (четное число): '))

window = turtle.Screen()
window.bgcolor("white")

snowflake = turtle.Turtle()
snowflake.color("#040A86")

snowflake.pensize(4)

snowflake.penup()
snowflake.goto(0, 40)
snowflake.pendown()

rotation_angle = random.randint(0, 360)
snowflake.setheading(rotation_angle)

draw_snowflake(snowflake, 150, branches)

snowflake.hideturtle()

window.mainloop()
