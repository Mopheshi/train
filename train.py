import math
import turtle

bob = turtle.Turtle()
print(bob)


def polyline(t, n, length, angle):
    """
    Draws n line segments with the given length and
    angle (in degrees) between them. t is a turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def circle(t, r):
    angle = 360
    arc(t, r, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle / n)

    polyline(t, n, step_length, step_angle)


square(bob, 50)
polygon(bob, 50, 10)
circle(bob, 50)
arc(bob, 50, 360)
turtle.mainloop()
