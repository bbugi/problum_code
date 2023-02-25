# 피보나치 수 2 (브1)
# https://www.acmicpc.net/problem/2748

'''
수학, 다이나믹 프로그래밍
'''


# ===== 문제 풀이 =====
# 문제에 나온 90까지만 피보나치 돌리면 되므로 리스트로 크기 제한을 걸어두고 시작

import sys
input = sys.stdin.readline

n = int(input())

fibo_list = [0] * 91 
# print(fibo_list)

fibo_list[1] = 1
fibo_list[2] = 1
for i in range(3, len(fibo_list)):
    fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]

print(fibo_list[n]) 




# ===== 문제 풀이 (그냥 재귀로 풀면 시간초과 나옴) =====

# import sys
# input = sys.stdin.readline

# n = int(input())

# def fibo(n):
#     if n <= 1 :
#         return n
#     return fibo(n-1)+fibo(n-2)

# print(fibo(n))