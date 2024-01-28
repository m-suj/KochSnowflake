from turtle import *
from math import sqrt

# Window Setup
setup(1920, 1080, 0, 0)
pencolor('red')
speed(0)

# Pen Setup
penup()
setpos(0, 0)
pendown()
tracer(0)


def draw_triangle(x, y, a, n):
    h = a * sqrt(3) / 3

    if n > 1:
        angle = 210

        for i in range(3):
            penup()
            setpos(x, y)
            setheading(angle)
            angle += 120
            forward(h/2)
            draw_triangle(pos()[0], pos()[1], a/2, n-1)

    penup()
    setpos(x, y)
    setheading(210)
    forward(h)
    right(30)
    pendown()

    for i in range(3):
        right(120)
        forward(a)


def draw_snowflake(x, y, a, n):
    penup()
    setpos(x, y)
    setheading(150)
    forward(a * sqrt(3) / 3)
    setheading(0)
    pendown()

    for i in range(3):
        draw_snowflake_side(a, n)
        right(120)


def draw_snowflake_side(a, n):
    if n == 0:
        forward(a)
        return
    a /= 3.0
    draw_snowflake_side(a, n - 1)
    left(60)
    draw_snowflake_side(a, n - 1)
    right(120)
    draw_snowflake_side(a, n - 1)
    left(60)
    draw_snowflake_side(a, n - 1)


# hideturtle()
# draw_triangle(0, 0, 1024, _n)
# showturtle()


for _n in range(8):
    draw_snowflake(0, 0, 512 + 52*_n, _n)
    update()

done()
