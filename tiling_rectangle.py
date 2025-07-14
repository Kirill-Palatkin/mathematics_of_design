import turtle
import random

# Настройки экрана
screen = turtle.Screen()
screen.bgcolor("white")

# Создание объекта черепашки
t = turtle.Turtle()
t.speed(0)  # Максимальная скорость рисования


# Функция для рисования прямоугольника
def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


# Функция для генерации случайного цвета из списка цветов
def random_color(colors):
    return random.choice(colors)


# Основная функция для замощения плоскости
def tile_plane(rows, cols, rect_width, rect_height, width, height, colors, offset_x):
    # Создание сетки для хранения цветов прямоугольников
    grid = [[None for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            # Перемещение черепашки в нужную позицию
            x = col * rect_width + offset_x
            y = row * rect_height

            # Проверка, находится ли прямоугольник внутри границ
            if -width / 2 <= x <= width / 2 and -height / 2 <= y <= height / 2:
                t.penup()
                t.goto(x, y)
                t.pendown()

                # Выбор цвета, который не совпадает с цветами соседей
                available_colors = colors[:]
                if row > 0:
                    neighbor_color = grid[row - 1][col]
                    if neighbor_color in available_colors:
                        available_colors.remove(neighbor_color)
                if col > 0:
                    neighbor_color = grid[row][col - 1]
                    if neighbor_color in available_colors:
                        available_colors.remove(neighbor_color)

                # Рисование прямоугольника со случайным доступным цветом
                color = random.choice(available_colors)
                draw_rectangle(rect_width, rect_height, color)
                grid[row][col] = color


# Параметры замощения
rows = 10
cols = 10
rect_width = 50
rect_height = 30
width = 600  # Ширина области замощения
height = 600  # Высота области замощения
colors = ["red", "green", "blue", "yellow"]  # Список цветов
offset_x = -250  # Смещение по оси X

# Запуск замощения
tile_plane(rows, cols, rect_width, rect_height, width, height, colors, offset_x)

# Завершение работы программы
turtle.done()
