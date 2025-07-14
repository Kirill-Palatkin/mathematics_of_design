import turtle

r = 'r'
l = 'l'

old = r
new = old

iteration = int(input('Кол-во итераций:'))
length = 10

cycle = 1

while cycle < iteration:
    new = (old) + (r)
    old = old[::-1]
    for char in range(0, len(old)):
        if old[char] == r:
            old = (old[:char]) + (l) + (old[char + 1:])
        elif old[char] == l:
            old = (old[:char]) + (r) + (old[char + 1:])
    new = (new) + (old)

    old = new
    cycle = cycle + 1

    print(cycle, 'итерация: ', new)

turtle.ht()
turtle.speed(0)
turtle.color('green')
turtle.bgcolor('white')

turtle.penup()
turtle.goto(30, 150)
turtle.pendown()

turtle.forward(length)

for char in range(0, len(new)):
    if new[char] == (r):
        turtle.right(90)
        turtle.forward(length)
    elif new[char] == (l):
        turtle.left(90)
        turtle.forward(length)

window = turtle.Screen()
window.exitonclick()
