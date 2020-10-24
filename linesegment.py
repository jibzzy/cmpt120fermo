# Introduction to Programming
# Week 8 Assignment 3
# October 23 2020

from graphics import *
from math import sqrt

def main():
    win = GraphWin('Line Segment Drawer', 300, 300)

    pt1 = win.getMouse()
    pt1.draw(win)
    pt2 = win.getMouse()
    line = Line(pt1, pt2)
    line.setWidth(2)
    line.draw(win)

    mid_x = (pt1.getX() + pt2.getX()) / 2
    mid_y = (pt1.getY() + pt2.getY()) / 2
    midpt = Circle(Point(mid_x, mid_y), 2)
    midpt.setOutline('red')
    midpt.setFill('red')
    midpt.draw(win)

    dx = pt2.getX() - pt1.getX()
    dy = pt2.getY() - pt1.getY()
    slope = - dy / dx
    length = sqrt(dx**2 + dy**2)

main()
