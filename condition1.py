# Introduction to Programming
# Module 5 Assignment 1
# October 2, 2020

def main():
    print('Calculation for a Speeding Violation')
    limit = int(input('Enter speed limit here: '))
    speed = int(input('Enter speed traveled here: '))

    if speed <= limit:
        print('\nYour speed was legal.')
    elif speed > limit and speed < 65:
        fine = 80 + (speed - limit)*3
        print('\nYour fine is $' + str(fine) + '.')
    else:
        fine = 200 + (speed - limit)*3
        print('\nYour fine will be $' + str(fine) + '.')

main()
