# Introduction to Programming
# Project 1
# 16 October 2020

def one_bit_adder(a,b,ci):
    if a > 1:
        print ("The number that you entered for the a value is not valid.")
    if b > 1:
        print ("The number that you entered for the b value is not valid.")
    if ci > 1:
        print ("The number that you entered for the carry input is not valid.")
    if (a) == 0 and (b) == 0 and (ci) == 0:
        return print ("The sum and carry ouput are 0,0")
    if (a) == 0 and (b) == 0 and (ci) == 1:
        return print ("The sum and carry output are 1,0")
    if (a) == 0 and (b) == 1 and (ci) == 0:
        return print ("The sum and carry output are 1,0")
    if (a) == 0 and (b) == 1 and (ci) == 1:
        return print ("The sum and carry output are 0,1")
    if (a) == 1 and (b) == 0 and (ci) == 0:
        return print ("The sum and carry output are 1,0")
    if (a) == 1 and (b) == 0 and (ci) == 1:
        return print ("The sum and carry output are 0,1")
    if (a) == 1 and (b) == 1 and (ci) == 0:
        return print ("The sum and carry output are 0,1")
    if (a) == 1 and (b) == 1 and (ci) == 1:
        return print ("The sum and carry output are 1,1")
    
    
        
    
    
            
                   
            
    
    
    
    
    
    
