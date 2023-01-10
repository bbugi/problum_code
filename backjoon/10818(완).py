# 최소, 최대 (브3)
# https://www.acmicpc.net/problem/10818

# =============== 문제 풀이 ================

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def min_max(n, nums):
    print(min(nums), max(nums))

min_max(n, nums)
