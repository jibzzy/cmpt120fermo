# logic_gates.py
# This file defines functions for all the logic gates
from graphics import *

def and_g(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def or_g(a,b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

def not_g(a):
    if a == 1:
        return 0
    else:
        return 1        

def nand_g(a,b):
    return not_g(and_g(a,b))

def xor_g(a,b):
    x = and_g(not_g(b),a)
    y = and_g(not_g(a),b)
    return or_g(x,y)
