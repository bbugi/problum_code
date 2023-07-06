import datetime

date_format = "%Y-%m-%d"

day1 = '2022-09-01'
day2 = '2022-09-01'


day11 = datetime.datetime.strptime(day1, date_format)
day22 = datetime.datetime.strptime(day2, date_format)

print((day22 - day11).days)