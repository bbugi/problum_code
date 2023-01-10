# 최댓값 (브3)
# https://www.acmicpc.net/problem/2562

# =============== 문제 풀이 =============

import sys
input = sys.stdin.readline

nums =[]

for i in range(9):
    nums.append(int(input()))
print(max(nums), (nums.index(max(nums))+1))