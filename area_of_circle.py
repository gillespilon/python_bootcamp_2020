#! /usr/bin/env python3

'''
area_of_circle.py

./area_of_circle.py
'''


import math


# Ask the user for the radius of a circle and then print the area
radius_of_circle = float(input('What is the radius of the circle? > '))
# print(radius_of_circle)
area_of_circle = math.pi * radius_of_circle**2
# print(area_of_circle)
print('You entered a radius of ', radius_of_circle)
print('The area of the circle is ', area_of_circle)
