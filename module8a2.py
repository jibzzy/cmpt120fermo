# Introduction to Programming
# Week 10 Module 8 Assignment 2
# October 30, 2020

from random import randrange

def main():
    n = GetN()
    wins = simNGames(n)
    printData(wins,n)

def GetN():
    n = eval(input("Enter the amount of Craps games you would like to simulate: "))
    return n

def simNGames(n):
    wins = 0
    for i in range(n):
        if winOneGame():
            wins += 1
        return wins

def winOneGame():
    roll_1 = randrange(1, 7) + randrange(1, 7)
    if roll_1 == 2 or roll_1 == 3 or roll_1 == 12:
        return False
    elif roll_1 == 7 or roll_1 == 11:
        return True
    else:
        roll = 0
        while roll != roll_1 and roll !=7:
            roll = randrange(1, 7) + randrange(1, 7)
            if roll == roll_1: #JA
                return True
            else:
                return False

def printData(wins, n):
    prob = wins / n
    print("\nEstimated Probability of Winning: {0:.1%}".format(prob))

if __name__ == '__main__':
    main()
    
    
