# 직사각형 네개의 합집합의 면적 구하기
# https://www.acmicpc.net/problem/2669

# 색종이 문제와 동일한 형식으로 풀이하기

# ========== 문제풀이 =========


full = [[0] * 100 for i in range(100)]

# print(full)


import sys
input = sys.stdin.readline

for i in range(4):