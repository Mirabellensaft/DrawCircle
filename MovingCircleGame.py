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

def isinCircle(tx,ty, r, dx, dy):

    """Checks, if coordinates of get_touch() are within the circle"""

    if tx in range(dx-r, dx+r) and ty in range(dy-r, dy+r):
        inCircle = True
    else:
        inCircle = False
    print (inCircle)
    return inCircle

def rRadius():
    radius = randint(10,30)
    return radius

def rOff(r, maximum):
    d = randint(0, maximum-r)
    return d

def rDir():
    m = randint(1,4)
    return m


def MovingCircle(r, dx, dy, mx, my, counter):

    while True:
        touch = lcd.get_touch()
        print (touch, r, dx, dy)
        if touch[0] == 1:
            if isinCircle(touch[1], touch[2], r, dx, dy) == True:
                counter += 1
                for i in range(r):
                    lcd.erase()
                    DrawCircle(r-i, dx, dy)

                fg = lcd.rgb(randint(0, 255), randint(0, 255), randint(0, 255))
                bg = lcd.rgb(randint(0, 255), randint(0, 255), randint(0, 255))
                writing = lcd.rgb(255, 255, 255)
                lcd.set_pen(fg, bg)
                lcd.erase()

                # lcd.set_pos(120, 150)
                lcd.set_text_color(writing, bg)
                # lcd.set_font(0, 8)



                r = rRadius()
                MovingCircle(r, rOff(r, 129), rOff(r, 159), rDir(), rDir(), counter)

        else:

            my = Direction(r, dy, my, 159)
            mx = Direction(r, dx, mx, 129)
            dy = dy+my
            dx = dx+mx
            lcd.erase()
            lcd.set_pos(1, 1)
            lcd.write('{}' .format(counter))
            DrawCircle(r, dx, dy)



counter = 0

fg = lcd.rgb(randint(0, 255), randint(0, 255), randint(0, 255))
bg = lcd.rgb(randint(0, 255), randint(0, 255), randint(0, 255))
writing = lcd.rgb(255, 255, 255)
lcd.set_pen(fg, bg)
lcd.erase()

lcd.set_pos(1, 1)
lcd.set_text_color(writing, bg)
lcd.set_font(0, 4, 0, 0, 0)
lcd.write('{}' .format(counter))

MovingCircle(30, 30, 60, 1, 2, counter)
