# 숫자의 개수(브2)
# https://www.acmicpc.net/problem/2577

'''
수학, 구현, 사칙연산 문제
'''

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

num = (a * b * c)
print(num)

num_l = [int(a) for a in str(num)]
print(num_l)

count = [0] * 10

for i in range(10):
    for j in range(len(num_l)):
        if i == num_l[j]:
            count[i] += 1

print(*count, sep='\n')