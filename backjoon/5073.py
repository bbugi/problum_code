# 삼각형과 세 변 (브3)
# https://www.acmicpc.net/problem/5073

'''
수학, 구현, 기하학
'''

import sys
input = sys.stdin.readline

while True :
    numbers = list(map(int, input().split()))
    numbers.sort(reverse=True)

    if set(numbers) == {0} :
        break
    elif len(set(numbers)) == 1 :
        print('Equilateral')
    elif numbers[0] == max(numbers) and numbers[0] >= numbers[1]+numbers[2] :
        print('Invalid')
    elif len(set(numbers)) == 2 :
        print('Isosceles ')
    else :
        print('Scalene')