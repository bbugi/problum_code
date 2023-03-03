# 피보나치 (실3)
# https://www.acmicpc.net/problem/9711

'''
수학, 다이나믹 프로그래밍
'''

# ===== 문제 풀이 =====

fibo = [0, 1]
for i in range(2, 10001):
    fibo.append(fibo[i-1]+fibo[i-2])
    
# print(fibo)

t = int(input())

for i in range(t):
    p, q = map(int, input().split())
    
    print(f"Case #{i+1}:", fibo[p]%q)




# ====== 시간초과 못잡음 ( 이중for문 사용해서 시간초과 난 것이었음!) =======

# import sys
# input = sys.stdin.readline

# # 테스트 케이스 입력
# T = int(input())
# for i in range(T):
#     P, Q = map(int, input().split())

# # 피보나치 수열 만들기
#     fibo = [0] * P
 
#     for j in range(len(fibo)):
#         if j <= 1:
#             fibo[j] = 1

#         else:
#             fibo[j] = fibo[j-1] + fibo[j-2]
#     # print(fibo)
#     M = fibo[P-1] % Q
#     print(f"Case #{i+1}: {M}")



# ==== 재귀함수 걸어서 만드니까 100 100 케이스에서 멈춤 ====

# T = int(input())

# def fibo(num):
#     if num <= 1:
#         return num
#     elif num <= 10000:
#         return fibo(num-1) + fibo(num-2)

# for i in range(T):
#     P, Q = map(int, input().split())

#     M = fibo(P) % Q
#     print(f"Case #{i+1}: {M}")