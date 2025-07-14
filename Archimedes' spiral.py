import turtle
import math

window = turtle.Screen()
window.bgcolor("white")

spiral = turtle.Turtle()
spiral.color("#00693E")
spiral.speed(0)
spiral.pensize(3)

a = 7
for angle in range(0, 360 * 10, 8):
    radians = math.radians(angle)
    x = a * radians * math.cos(radians)
    y = a * radians * math.sin(radians)
    spiral.goto(x, y)


window.mainloop()
