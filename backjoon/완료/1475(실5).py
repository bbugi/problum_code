# 방 번호 (실5)
# https://www.acmicpc.net/problem/1475

'''
구현
'''

n = list(input())

numbers = [0] * 10

for i in n :
    i = int(i)
    if i == 9 :
        numbers[6] += 1
    else:
        numbers[i] += 1

if numbers[6] % 2 == 0:
    numbers[6] = numbers[6] // 2
else:
    numbers[6] = numbers[6] // 2 + 1

print(max(numbers))