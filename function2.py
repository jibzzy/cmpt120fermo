# Assignment 7
# Introduction to Programming
# 25 September 2020

import math

def sphereArea(radius):
    return 4 * math.pi * radius ** 2

def sphereVolume(radius):
    return (4/3) * math.pi * radius **3

def main():
    print('Module 2')
    rad = eval(input('Enter a radius: '))

    print('Surface Area:', sphereArea(rad))
    print('Volume:', sphereVolume(rad))

main()

