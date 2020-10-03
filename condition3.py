# Introduction to Programming
# Module 5 Assignment #3
# October 2, 2020

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap

def is_valid_date(date):
    is_valid = True
    thirty_one_day_months = [1, 3, 5, 7, 8, 10, 12]

    date_list = date.split('/')
    if len(date_list) !=3:
        is_valid = False
    else: month, day, year = date_list

    try:
            month = int(month)
            day = int(day)
            year = int(year)

            if month > 12 or month < 1 or day > 31 < 1 or year < 1:
                is_valid = False
            elif month not in thirty_one_day_months and day == 31:
                is_valid = False

            if is_leap(year) and month == 2 and day == 30:
                is_valid = False
            elif not is_leap(year) and month == 2 and day > 28:
                is_valid = False
    except:
            is_valid = False
    return is_valid

def main():
    date = input('Enter a date here: ')

    if not is_valid_date(date):
        print("The date entered is not valid.")
    else:
        month, day, year = date.split('/')
        month = int(month)
        day = int(day)
        year = int(year)

        dayNum = 31*(month - 1) + day
        dayNum -= round(4*month + 23) /10
        if is_leap(year) and month > 2:
            dayNum += 1

        print('The day number for that date is', str(dayNum) + '.')

main()
