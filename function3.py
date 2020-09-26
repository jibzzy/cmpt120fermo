# Assignment 6
# Introduction to Computer Sciente
# 25 September 2020


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])

def main():
    list_of_lists = [['2'], ['1','2','4','10'], ['-1','-6','1','6'],\
                     ['1.1','2.2']]
    print(list_of_lists)

    for lst in lists_of_lists:
        toNumbers(lst)
    print(list_of_lists)

main()
