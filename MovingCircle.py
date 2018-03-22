import pyb
import lcd160cr
from math import sqrt # so we don't need to resolve math.sqrt on every loop iteration later
from random import randint

lcd = lcd160cr.LCD160CR('X')

def DrawCircle(r, dx, dy):
    """r = radius of the circle
    dx and dy are offset in x and y
    so the circle's center is not at 0,0"""

    for x in range(0, r):
        if x/(sqrt(r**2-x**2)) < 1:
            y = round(sqrt(r**2-x**2))

            lcd.dot(dx + x, dy - y) #1
            lcd.dot(dx + y, dy - x) #2
            lcd.dot(dx + y, dy + x) #3
            lcd.dot(dx + x, dy + y) #4
            lcd.dot(dx - x, dy + y) #5
            lcd.dot(dx - y, dy + x) #6
            lcd.dot(dx - y, dy - x) #7
            lcd.dot(dx - x, dy - y) #8


def Direction(r, d, m, maximum):
    """determines the sign of the slope values
    and thus the direction the circle is moving"""

    if d-r <= 0:
        m = abs(m)
    elif d+r >= maximum:
        m = -m
    else:
        m = m
    return m


def MovingCircle(r, dx, dy, mx, my):

    while True:
        my = Direction(r, dy, my, 159)
        mx = Direction(r, dx, mx, 129)
        dy = dy+my
        dx = dx+mx
        lcd.erase()
        DrawCircle(r, dx, dy)

fg = lcd.rgb(randint(0, 255), randint(0, 255), randint(0, 255))
bg = lcd.rgb(randint(0, 255), randint(0, 255), randint(0, 255))

lcd.set_pen(fg, bg)
lcd.erase()

MovingCircle(30, 30, 60, 1, 2, counter)
