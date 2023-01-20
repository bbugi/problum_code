# 동전 0 (실4)
# https://www.acmicpc.net/problem/11047

'''
그리디 알고리즘
'''

# ==== 문제 풀이 =====

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
count = 0
for _ in range(n):
    coins.append(int(input()))
coins.reverse()
# print(coins)

for coin in coins:
    count += k // coin
    k = k % coin

print(count)