import pyb
import lcd160cr
from math import sqrt # so we don't need to resolve math.sqrt on every loop iteration later

lcd = lcd160cr.LCD160CR('X')

def DrawCircle(r, dx, dy):
    """r = radius of the circle
        dx and dy are offset in x and y
        so the circle's center is not at 0,0"""

    for x in range(0, r):
        y = round(sqrt(r**2-x**2)) # do expensive operations only once

        # but addition is cheap:
        lcd.dot(dx + x, dy + y)
        lcd.dot(dx + x, dy - y)
        lcd.dot(dx - x, dy + y)
        lcd.dot(dx - x, dy - y)

lcd.set_pen(lcd.rgb(255, 0, 0), lcd.rgb(64, 64, 128))
lcd.erase()
DrawCircle()
