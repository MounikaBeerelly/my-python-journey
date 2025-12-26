import os
import calendar

os.system("cls")

print(calendar.firstweekday()) # 0
print(calendar.isleap(2024)) # True
print(calendar.leapdays(2000, 2020)) # 5
print(calendar.month(2021, 9, 3, 1))
print(calendar.monthrange(2021,9)) # (2, 30) 2 -> weekday of the month starting day, 30 -> number of days 
print(calendar.weekday(2021, 9, 29)) # 2

