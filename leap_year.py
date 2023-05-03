
def is_leap(year):
    #divid the year by 100 if it is dividable
    if not (year % 100):
        year = year // 100

    #divid the year by 4 to check for dividable by 4 case
    #in case it is dividable by 100 , it already divided by 100 so i divided by 4 only
    leap = not (year % 4)
    return leap

#ask the user to enter the year
year = int(input('Enter a year: '))


#output
if is_leap(year):
    print ('the year is leap year')
else:
    print('the year is not leap year')