# 피보나치 수 2 (브1)
# https://www.acmicpc.net/problem/2748

'''
수학, 다이나믹 프로그래밍

다이나믹 프로그래밍 ( 메모이제이션 )
한번 계산한 값은 저장해둬서 한번에 불러올 수 있게 하는 것
== 리스트에 계산한 값을 


'''


# ===== 문제 풀이 =====
# 문제에 나온 90까지만 피보나치 돌리면 되므로 리스트로 크기 제한을 걸어두고 시작

# bottom-up 방식
# 밑에서부터 계산해서 쌓아가는 방식

# import sys
# input = sys.stdin.readline

# n = int(input())

# # fibo_list = [0] * 91 
# fibo_list = [0] * n+1
# # print(fibo_list)

# fibo_list[1] = 1
# fibo_list[2] = 1
# for i in range(3, len(fibo_list)):
#     fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]

# print(fibo_list[n]) 


# ==== top-down 방식
# 메모이제이션

n = int(input())

mem = [0] * (n+1)
def fibonacci(num):
  if num <= 1:
    return num
  if mem[num] != 0:
    return mem[num]
  mem[num] = fibonacci(num-1) + fibonacci(num-2)
  return mem[num]

print(fibonacci(n))




# ===== 문제 풀이 (그냥 재귀로 풀면 시간초과 나옴) =====

# import sys
# input = sys.stdin.readline

# n = int(input())

# def fibo(n):
#     if n <= 1 :
#         return n
#     return fibo(n-1)+fibo(n-2)

# print(fibo(n))