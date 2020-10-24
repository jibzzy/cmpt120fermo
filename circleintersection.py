# Introduction to Programming
# Week 8 Assignment #2
# October 23, 2020

import math

def checkCollision(a, b, c, x, y, radius):

    dist = ((abs(a * x + b * y + c)) /
            math.sqrt(a * a + b * b))

    if (radius ==dist):
        print("Touch")
    elif (radius > dist):
        print ("Intersect")
    else:
        print ("Outside")


radius = 5
x = 0
y = 0
a = 3
b = 4
c = 25
checkCollision(a, b, c, x, y, radius)
