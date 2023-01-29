# 수 정렬하기2 (실5)
# https://www.acmicpc.net/problem/2751

# for문 안에서 sort 돌리면 for문 돌릴때마다 sort 하기때문에
# 시간이 더 많이 걸리게 된다 (런타임에러 발생)

# =============== 문제 풀이 ============

import sys
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
for i in sorted(nums): # num.sort() 말고 다른 방식으로 정렬해봄!
    print(i)