# Introduction to Programming
# Week 10 Assignment
# Vincent Fermo

from random import randrange

def main():
    n = eval(input("Enter the amount of times a 5 dice will be rolled: "))

    wins = 0
    for i in range(n):
        d1 = randrange(1, 7)
        d2 = randrange(1, 7)
        d3 = randrange(1, 7)
        d4 = randrange(1, 7)
        d5 = randrange(1, 7)
        if d1 == d2 and d1 == d3 and d1 == d4 and d1 == d5:
            wins += 1

    prob = wins/ n
    print("The estimated probability of a 5-of-a-kind: {0:0.4%}".format(prob))

main()
