import time
import os
import datetime
os.system("cls")

# Find start and end time of the program
startTime = time.time()
time.sleep(1)
endTime = time.time()
print(endTime - startTime)

print(time.process_time())
print(time.perf_counter())
print(time.ctime()) # returns current time

currentDate = datetime.date.today()
dateTimeTuple = currentDate.timetuple()
print(dateTimeTuple) # time.struct_time(tm_year=2025, tm_mon=12, tm_mday=23, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=357, tm_isdst=-1)
print("The current year is : ", currentDate.timetuple()[0])
print("The current month is : ", currentDate.timetuple()[1])
print("The current day is : ", currentDate.timetuple()[2])

localTime = time.localtime(time.time())
print(localTime) # time.struct_time(tm_year=2025, tm_mon=12, tm_mday=24, tm_hour=11, tm_min=55, tm_sec=8, tm_wday=2, tm_yday=358, tm_isdst=0)
localTime = time.asctime(time.localtime(time.time()))
print(localTime) # Wed Dec 24 11:55:08 2025
myTimeTuple = (2025, 12, 24, 11, 55, 8, 2, 358, 0)
myTimeValue = time.mktime(myTimeTuple)
print(myTimeValue)#1766598908.0
print(time.strftime("%b %d %Y %H:%M:%S", time.localtime(myTimeValue)))#Dec 24 2025 11:55:08
print(time.strftime("%a", time.localtime(myTimeValue)))#Wed
print(time.strftime("%A", time.localtime(myTimeValue)))#Wednesday
print(time.strftime("%b", time.localtime(myTimeValue)))#Dec
print(time.strftime("%B", time.localtime(myTimeValue)))#December
print(time.strftime("%c", time.localtime(myTimeValue)))#Wed Dec 24 11:55:08 2025
print(time.strftime("%C", time.localtime(myTimeValue)))#20 - current century
print(time.strftime("%d", time.localtime(myTimeValue)))#24
print(time.strftime("%e", time.localtime(myTimeValue)))#24
print(time.strftime("%g", time.localtime(myTimeValue)))#20 - current century
print(time.strftime("%G", time.localtime(myTimeValue)))#2025 - full year
print(time.strftime("%H", time.localtime(myTimeValue)))# 11 - 24 hours mode
print(time.strftime("%T", time.localtime(myTimeValue)))#11:55:08
print(time.strftime("%W", time.localtime(myTimeValue)))#51 - week number of the current year

myStructTime = time.strptime("24 12 2025", "%d %m %Y")
print("The struct time tuple : ", myStructTime ) # time.struct_time(tm_year=2025, tm_mon=12, tm_mday=24, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=358, tm_isdst=-1)








