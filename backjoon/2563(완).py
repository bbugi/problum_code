# 색종이 (실5)
# https://www.acmicpc.net/problem/2563

# 다시 풀어보기 (완료)

# ================ 문제 풀이 ===============

# numpy를 사용하지 않고 0으로 초기화된 2차원 행렬 생성

import sys
input = sys.stdin.readline
paper = [[0]*100 for _ in range(100)]

count = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if paper[i][j] != 1:
                paper[i][j] = 1
                count += 1
        else:
            pass

print(count)


# ==========================