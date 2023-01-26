# 피보나치 수(브2)
# https://www.acmicpc.net/problem/2747

import sys
input = sys.stdin.readline

n = int(input())

a = 0
b = 1

while n > 0:
    a, b = b, a+b
    n -= 1

print(a)











# ===== 재귀함수 사용시 시간 초과 =====
# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-1) + fibo(n-2)
# print(fibo(n))
