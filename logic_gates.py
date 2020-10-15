# Introduction to Programming
# Project 1
# 16 October 2020

def and_g(a,b):
    if a > 1:
        print("Number entered is not valid.")
    else:
        return (a)

def or_g(a,b):
    if a > 1:
        print("Number entered is not valid.")
    if b > 1:
        print("Number entered is not valid.")
    else:
        if a >= b:
            return (a)
        if b >= a:
            return (b)

def not_g(a):
    if a == 1:
        return 0
    else:
        return 1

def nand_g(a,b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1

def xor_g(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

              


