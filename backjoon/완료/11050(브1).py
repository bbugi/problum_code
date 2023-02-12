# 이항 계수 1 (브1)
# https://www.acmicpc.net/problem/11050

'''
자연수 N과 정수 K가 주어졌을 때 이항 계수 N/K를 구하시오

이항 계수 - 조합론
nCk = n!/(n-k)!*k!

이항계수의 개념 : n개의 품목 중에 k개의 아이템을 뽑는 조합의 수

[참조블로그]
https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients

'''



# ====== 문제 풀이 ======


# 1. 팩토리얼 활용하기
# 1-1) 팩토리얼 함수로 직접 구현하기

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans


def bino_coef_factorial(n, k): # 이항 계수 : Binomial coefficient
    return factorial(n) // (factorial(n-k) * factorial(k))

n, k = map(int, input().split())
print(bino_coef_factorial(n, k))



# 2. 동적 계획법 ( 이항 계수 성질 이용하기 ) : 기억하며 풀기
# 어떻게 구현되는지 모르겠는걸..?

# def bino_coef(n, k):
#     if k == 0 or n == k:
#         return 1
#     return( bino_coef(n-1, k) + bino_coef(n-1, k-1) )

# n, k = map(int, input().split())
# print(bino_coef(n, k))


# 3. 조합의 수라고 하는데 combination도 가능한지? - 통과 됨
# from itertools import combinations

# n, k = map(int, input().split())

# item = [i for i in range(n)]
# # print(item)

# print(len(list(combinations(item, k))))