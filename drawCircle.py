import pyb
import lcd160cr
import math

lcd = lcd160cr.LCD160CR('X')

def DrawCircle(r, dx, dy):
    """r = radius of the circle
        dx and dy are offset in x and y
        so the circle's center is not at 0,0"""

    lcd.dot(dx+r, dy+r)
    for x in range(-r, r+1, 1):
        z = math.sqrt(r**2-x**2)
        y = -math.sqrt(r**2-x**2)
        z = round(z)
        y = round(y)
        print (x, z)
        print (x, y)

        lcd.dot(x+r+dx, z+r+dy)
        lcd.dot(x+r+dx, y+r+dy)

lcd.set_pen(lcd.rgb(255, 0, 0), lcd.rgb(64, 64, 128))
lcd.erase()
DrawCircle()
