# 색종이 (실5)
# https://www.acmicpc.net/problem/2563

# ================ 문제 풀이 ===============

# numpy를 사용하지 않고 0으로 초기화된 2차원 행렬 생성
paper = [[0 for _ in range(100)] for _ in range(100)]

array = [[0]*100 for _ in range(100)]

for _ in range(100):
    row = list(map(int, range(100)))
    full.append(row)
    
# 배열 안의 값 0으로 변경
for a in range(100):
    for b in range(100):
        full[a][b] = 0
