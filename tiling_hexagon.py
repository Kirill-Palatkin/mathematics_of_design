import turtle
import random

# Настройки экрана
screen = turtle.Screen()
screen.bgcolor("white")

# Создание объекта черепашки
t = turtle.Turtle()
t.speed(0)  # Максимальная скорость рисования

# Функция для рисования шестиугольника
def draw_hexagon(side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(6):
        t.forward(side_length)
        t.right(60)
    t.end_fill()

# Функция для генерации случайного цвета
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Основная функция для замощения плоскости
def tile_plane(rows, cols, side_length, width, height, offset_x):
    for row in range(rows):
        for col in range(cols):
            # Перемещение черепашки в нужную позицию
            x = col * side_length * 1.5 + offset_x
            y = row * side_length * 1.732 - (side_length * 0.866 * (col % 2))

            # Проверка, находится ли шестиугольник внутри границ
            if -width / 2 <= x <= width / 2 and -height / 2 <= y <= height / 2:
                t.penup()
                t.goto(x, y)
                t.pendown()

                # Рисование шестиугольника со случайным цветом
                draw_hexagon(side_length, random_color())

# Параметры замощения
rows = 10
cols = 10
side_length = 30
width = 600  # Ширина области замощения
height = 600  # Высота области замощения
offset_x = -210  # Смещение по оси X

# Запуск замощения
tile_plane(rows, cols, side_length, width, height, offset_x)

t.hideturtle()
# Завершение работы программы
turtle.done()
