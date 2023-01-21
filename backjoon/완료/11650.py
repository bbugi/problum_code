# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650


'''
정렬할때 인자가 2개이상일때 인자 순서대로 정렬하려면
sorted(리스트, key = lambda x : (x[0], x[1]) )

'''

# ======= 문제 풀이 ========
import sys
input = sys.stdin.readline

n = int(input())
m = []

for _ in range(n):
    x, y = map(int, input().split())
    m.append([x,y])
    # print(x, y)

num_sort = sorted(m, key = lambda x : (x[0], x[1]))
for i in range(n):
    print(*num_sort[i], end='\n')
# print(*num_sort, sep="\n")


