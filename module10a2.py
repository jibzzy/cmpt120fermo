# Introduction to Programming
# Module 10 Assignment 2
# 11/13/20

from random import randrange

def shuffle(myList):
    newList = []
    while len(myList) > 0:
        ind = randrange(len(myList))
        newList.append(myList.pop(ind))
    myList[:] = newList

add myList[ind] to newList
remove myList[ind] from myList
