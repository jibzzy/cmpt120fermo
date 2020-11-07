# Introduction to Programming
# November 6, 2020
# Project 2

from graphics import *

def draw_not(x, y, size, window):
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)
    vertices = []
    for i in range(3):                         
        x = random.randint(0, 500)             
        y = random.randint(0, 500)             
        vertices.append(graphics.Point(x, y))  
    triangle = graphics.Polygon(vertices)      
    triangle.setFill(colour)
    triangle.draw(win)
    Line(Point(x1,y1),Point(x1,y2)).draw(win)

def draw_xor(x,y,size,window):
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    Arc(Point(x1,y3),Point(x+size,y3)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

def draw_nand(x,y,size,window):
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    Arc(Point(x1,y3),Point(x+size,y3)).draw(win)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse()
    win.close()
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)
    
    
    
    
