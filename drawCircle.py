#import pyb
#import lcd160cr
from math import sqrt # so we don't need to resolve math.sqrt on every loop iteration later

#lcd = lcd160cr.LCD160CR('X')

def DrawCircle(r, dx, dy):
    """r = radius of the circle
        dx and dy are offset in x and y
        so the circle's center is not at 0,0"""

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


# lcd.set_pen(lcd.rgb(255, 0, 0), lcd.rgb(64, 64, 128))
# lcd.erase()
DrawCircle(30, 50, 60)
