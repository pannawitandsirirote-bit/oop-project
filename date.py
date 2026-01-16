def is_leap_year(year):
    leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return leap_year

def day_of_year(day, month, year):
    month_list = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    ans = sum(month_list[:month-1]) 
    ans += day
    if is_leap_year(year) and month > 2: 
        ans += 1
        
    return ans

def day_in_year(year):
    return 366 if is_leap_year(year) else 365



month_list = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
try:
    enter = input("Enter Input: ")
except ValueError : 
    print("Invalid input")
    exit()
x = enter.split(",")

y = enter.replace(",","-").split("-")
z = [int(i) for i in y] 

if z[1]>12 or z[4] > 12:
    print("Invalid")
    exit()
if z[0] > month_list[z[1]-1] or z[3] > month_list[z[4]-1]:
    print("Invalid")
    exit()
if (is_leap_year(z[2]) == False and z[1] == 2 and z[0]>28) or (is_leap_year(z[5]) == False and z[4]==2 and z[3]>28):

    print("Invalid")
    exit()

