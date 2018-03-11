#!/usr/bin/python
import time
import datetime
import calendar
print("Milliseconds lapsed since jan 1970 ",time.time())
print("Current local time ",time.localtime(time.time()))
print("Printing formated date time ",time.asctime(time.localtime(time.time())))
print("Printing current month calendar ")
now = datetime.datetime.now()
print(calendar.month(now.year,now.month))