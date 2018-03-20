import math

def DrawCircle():
    # lcd.set_pen(lcd.rgb(255, 0, 0), lcd.rgb(64, 64, 128))
    # lcd.erase()
    a = 10
    b = 10
    for x in range(-10, 10, 1):
        z = math.sqrt(100-x**2)
        y = -math.sqrt(100-x**2)
        z = round(z)
        y = round(y)
        print (x+a, z+b)
        print (x+a, y+b)

DrawCircle()
