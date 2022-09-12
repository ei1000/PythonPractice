#Given the radius of a circle and the area of a square, 
#return True if the circumference of the circle is greater than the square's perimeter 
# and False if the square's perimeter is greater than the circumference of the circle.

from math import *

radius = float(input("Input the radius of the circle: "))
area = float(input("Input the area of the square: "))

square_per = sqrt(area)*4
circle_cir = 2*pi*radius

radius_area = (radius, area)

print(radius_area, "->", (circle_cir >= square_per))
