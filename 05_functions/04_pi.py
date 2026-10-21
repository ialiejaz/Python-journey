import math

def circle_calc(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi * radius
    return area, circumference

a,c = circle_calc(2)

print(f"Area: {a.__round__(2)}, Circumference: {c.__round__(2)}")