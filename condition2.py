# Introduction to Programming
# Module 5 Assignment #2
# October 2, 2020

def main():
    year = int(input('Enter a year in between 1982 & 2048: '))

    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) %7

    day = 22 + d + e

    if day > 31:
        print('Easter falls on April', day - 31, 'in the year', \
              str(year) + '.')
    else:
        print('Easter falls on March', day, 'in the year', str(year) + '.')

main()
