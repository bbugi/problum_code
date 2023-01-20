# 직사각형 네개의 합집합의 면적 구하기 (브1)
# https://www.acmicpc.net/problem/2669

# 색종이 문제와 동일한 형식으로 풀이하기

# ========== 문제풀이 =========

import sys
input = sys.stdin.readline

full = [[0] * 100 for i in range(100)]

result = 0

for _ in range(4):
    temp = list(map(int, input().split()))
    # print(temp)
    for i in range(temp[0], temp[2]):
        for j in range(temp[1], temp[3]):
            # print(i, j)
            if full[i][j] == 0:
                full[i][j] = 1
                result += 1
            else:
                pass

print(result)
