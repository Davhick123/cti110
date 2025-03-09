# David Hicks
# Date
# P2LAB1 - Circle Calculations
# This program calculates and displays the diameter, circumference, and area of a circle based on user input.

import math

radius = float(input("What is the radius of the circle?: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"The diameter of the circle is: {diameter:.1f}")
print(f"The circumference of the circle is: {circumference:.2f}")
print(f"The area of the circle is: {area:.3f}")