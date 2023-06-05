import datetime

my_time = datetime.time(13, 20, 1, 20)
print(my_time.minute)
print(my_time.hour)
print(my_time)
print(type(my_time))
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())

from datetime import datetime

my_date_time = datetime(2021, 10, 3, 14, 20, 1)
print(my_date_time)
print(my_date_time.replace(year=2020))

from datetime import date

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
result = date1 - date2
print(type(result))
print(result.days)

datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)
my_diff = datetime1-datetime2
print(my_diff)
print(my_diff.days)
