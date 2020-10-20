# bit_adder.py
from logic_gates import *

def bit_adder(a,b,cIn):
    o1 = xor_g(a,b)
    s = xor_g(o1,cIn)
    and1 = and_g(o1,cIn)
    and2 = and_g(a,b)
    cOut = or_g(and1,and2)
    return s,cOut

