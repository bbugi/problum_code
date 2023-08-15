# 카드 2 (실4)
# https://www.acmicpc.net/problem/2164

''' 자료구조 (큐) '''

from collections import deque

n = int(input())

d = deque( i for i in range(1, n+1))

while len(d) != 1:
    d.popleft()
    d.append(d.popleft())

print(d[0])


