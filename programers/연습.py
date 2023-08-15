# import datetime

# date_format = "%Y-%m-%d"

# day1 = '2022-09-01'
# day2 = '2022-09-01'


# day11 = datetime.datetime.strptime(day1, date_format)
# day22 = datetime.datetime.strptime(day2, date_format)

# print((day22 - day11).days)


# from collections import deque

# d = deque([1,2,3,4,5,6])

# print(d)
# d.rotate(3)
# print(d)


angles = []
for i in range(3):
    angles.append(int(input()))

if sum(angles) != 180:
    print('Error')

elif set(angles).pop() == 60:
    print('Equilateral')

else :
    if len(set(angles)) == 3:
        print('Scalene')
    else:
        print('Isosceles')