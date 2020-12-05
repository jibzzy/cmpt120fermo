# Introduction to Programming
# Project 3 Part 1
# December 4th, 2020

class DigitalValue():
    def __init__(self, p, value):
        self.p = Point(p.getX(), p.getY())
        self.value = value

        while self.value !=0 and self.value !=1:
            self.value = int(input('Incorrect input, the value must be either 0 or 1:'))


    def getValue(self):
        return self.value


    def setValue(self, value):
        while value !=0 and value !=1:
            value = int(input('Incorrect input, value must be either 0 or 1:'))

        self.value = value


    def draw(self,win, type):

        if type == 'I':
            Entry(self.p,15).draw(win)

        elif type == 'o':
            Text(self.p, 'Hello').draw(win)

        else:
            print('Incorrect input, type must be I or O')


# Program that draws logic gates

from graphics import *

def draw_and(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4

    Line(Point(x1,y1),Point(x1,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)

    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10y)).draw(win)

def draw_or(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4

    Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)

    Line(Point(x1,y3),Point(x-2,y3)).draw(win)
    Line(Point(x1,y4),Point(x-2,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

def main():
    win = GraphWin()
    draw_and(50,50,60,win)
    draw_or(50,150,60,win)
    win.getMouse()

def draw_not(x, y, size, win):
    x1,x2 = x-size/2, x+size/2
    y1,y2 = y-size/2, y+size/2
    y3,y4 = y-size/4, y+size/4

    line(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win))
    Line(Point(x1,y1),Point(x2,y)).draw(win)
    Line(Point(x1,y2),Point(x2,y)).draw(win)
    circle(Point(x1,y),radius(x1+x2)/2(y1+y2/2))

    Line(Point(x1,y),Point(x-2,y)).draw(win)
    Line(Point(x+size,y),Point(x+size+10y)).draw(win)

def draw_xor(x,y,size,win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4

    Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
    Arc(Point(x1-size/2,y1-2),Point(x1+size/2,y2-2)).draw(win)
    Arc(Point(x1,y1),Point(x2,y)).draw(win)
    Arc(Point(x1,y2),Point(x2,y)).draw(win)

    Line(Point(x1,y3),Point(x-2,y3)).draw(win)
    Line(Point(x1,y4),Point(x-2,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

def draw_nand(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2, y+size/2
    y3,y4 = y-size/4, y+size/4

    Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    circle(Point(x1,y),radius(x1+x2)/2(y1+y2/2))

    Line(Point(x1,y3),Point(x-2,y3)).draw(win)
    Line(Point(x1,y4),Point(x-2,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

class AndGate(BinaryGate):

    def __init__(self,n):
        (AndGate,self).__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
    g1 = AndGate("G1")
    g1.getOutput()
    print = ("Enter Pin A for gate G1") + input
    print = ("Enter Pin B for gate G1") + input

Class AndGate(BinaryGate):

    def __init__(self,n):
        (AndGate,self).__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
    g1 = AndGate("G1")
    g1.getOutput()
    print = ("Enter Pin A for gate G1") + input
    print = ("Enter Pin B for gate G1") + input

class OrGate(BinaryGate):

    def __init__(self,n):
        (OrGate,self).__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
    g1 = OrGate("G1")
    g1.getOutput()
    print = ("Enter Pin A for gate G1") + input
    print = ("Enter Pin B for gate G1") + input

class NotGate(BinaryGate):

    def __init__(self, n):

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
    g1 = NotGate("G1")
    g1.getOutput()
    print = ("Enter Pin A for gate G1") + input
    print = ("Enter Pin B for gate G1") + input

class xorGate(BinaryGate):

    def __init__(self, n):
        (XorGate,self).__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
    g1 = XorGate("G1")
    g1.getOutput()
    print = ("Enter Pin A for gate G1") + input
    print = ("Enter Pin B for gate G1") + input

class NandGate(BinaryGate):

    def __init__(self, n):
        (NandGate,self).__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
    g1 = NandGate("G1")
    g1.getOutput()
    print = ("Enter Pin A for gate G1") + input
    print = ("Enter Pin B for gate G1") + input


    
    
    
    
        
    
        
        


        
    

    
    

    
