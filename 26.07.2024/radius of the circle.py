import math
def area_of_circle(radius):
    return math.pi * (radius ** 2)

radius = input()
print(f"Area of the circle with radius {radius} is {area_of_circle(radius)}")
