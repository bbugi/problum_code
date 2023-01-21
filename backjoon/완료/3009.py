# 네 번째 점 (브3)
# https://www.acmicpc.net/problem/3009

'''
구현, 기하학 문제

직사각형의 3개의 점이 주어졌을 때 4번째의 점의 좌표 출력하기
3개의 좌표중 1개만 존재하는 숫자를 출력
'''


# ====== 문제 풀이 ======

import sys
input = sys.stdin.readline
square_x = [0] * 1001
square_y = [0] * 1001

for i in range(3):
    x, y = map(int, input().split())
    square_x[x] += 1
    square_y[y] += 1
    
print(square_x.index(1), square_y.index(1))