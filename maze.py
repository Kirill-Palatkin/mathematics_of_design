import tkinter as tk
import random

CELL_SIZE = 20


def create_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    start_x, start_y = 1, 1
    maze[start_y][start_x] = 0
    stack = [(start_x, start_y)]

    while stack:
        x, y = stack[-1]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        moved = False
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy][x + dx] = 0
                stack.append((nx, ny))
                moved = True
                break

        if not moved:
            stack.pop()

    maze[1][0] = 0
    maze[height - 2][width - 1] = 0

    return maze


def draw_maze(canvas, maze, cell_color):
    canvas.delete("all")
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE,
                                        (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                                        fill="black")
            else:
                canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE,
                                        (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                                        fill=cell_color)

    canvas.create_rectangle(0 * CELL_SIZE, 1 * CELL_SIZE,
                            (0 + 1) * CELL_SIZE, (1 + 1) * CELL_SIZE,
                            fill="red")

    canvas.create_rectangle((len(maze[0]) - 1) * CELL_SIZE, (len(maze) - 2) * CELL_SIZE,
                            (len(maze[0])) * CELL_SIZE, (len(maze) - 1) * CELL_SIZE,
                            fill="green")


def generate_new_maze():
    try:
        width_str = width_entry.get()
        height_str = height_entry.get()

        if not width_str or not height_str:
            raise ValueError("Поля ввода не должны быть пустыми.")

        width = int(width_str)
        height = int(height_str)

        if width < 5 or height < 5:
            raise ValueError("Размеры лабиринта должны быть не менее 5.")
    except ValueError as e:
        error_label.config(text=str(e))
        return

    maze = create_maze(width, height)
    cell_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    draw_maze(canvas, maze, cell_color)
    canvas.config(width=width * CELL_SIZE, height=height * CELL_SIZE)
    error_label.config(text="")


root = tk.Tk()

width_label = tk.Label(root, text="Ширина лабиринта:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()
width_entry.insert(0, "20")

height_label = tk.Label(root, text="Высота лабиринта:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()
height_entry.insert(0, "20")

new_maze_button = tk.Button(root, text="Новый лабиринт", command=generate_new_maze)
new_maze_button.pack()

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

canvas = tk.Canvas(root, width=20 * CELL_SIZE, height=20 * CELL_SIZE)
canvas.pack()

error_label.config(text="")

generate_new_maze()

root.mainloop()
