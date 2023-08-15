# 가격 (브2)
# https://www.acmicpc.net/problem/11296

'''
수학, 구현, 사칙연산
'''

color = ['R','G','B','Y','O','W']
sales = [0.45, 0.3, 0.2, 0.15, 0.1, 0.05]

n = int(input())

for _ in range(n):
    lst = list(map(str, input().split()))
    for ci in range(len(color)) :
        if lst[1] == color[ci] :
            money = float(lst[0]) * (1-sales[ci])
    if lst[2] == 'C' :
        money = money * 0.95
    if lst[3] == 'C' :
        money = int(money * 100)
        if money % 10 <= 5 :
            money -= money % 10
            money = float(money / 100)
        else:
            money = (money + 10) - (money % 10)
            money = float(money / 100)
 
    print('${:.2f}'.format(round(money, 2)))