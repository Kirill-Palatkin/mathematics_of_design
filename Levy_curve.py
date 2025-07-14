import turtle


def draw_levy_curve(t, order, size):
    t.width(2)
    t.hideturtle()
    if order == 0:
        t.forward(size)
    else:
        t.left(45)
        draw_levy_curve(t, order - 1, size / (2 ** 0.5))
        t.right(90)
        draw_levy_curve(t, order - 1, size / (2 ** 0.5))
        t.left(45)


def rotate_square(t, angle):
    t.right(angle)


def main():
    order = int(input('Кол-во итераций (четное): '))
    angle = int(input('Угол поворота: '))
    window = turtle.Screen()
    window.setup(width=1000, height=800)

    t = turtle.Turtle()
    t.speed(0)
    size = 400
    fractal_size = size / (2 ** (order / 2))

    rotate_square(t, angle)

    start_x = (-fractal_size - 310) / 2
    start_y = (-fractal_size - 200) / 2

    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    draw_levy_curve(t, order, size)

    window.mainloop()


if __name__ == "__main__":
    main()
