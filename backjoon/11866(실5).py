# 요세푸스 문제0 (실5)
# https://www.acmicpc.net/problem/11866

'''
큐, 자료구조, 구현 문제
'''
from collections import deque
n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])

print('<', end='')

for i in range(n):
    for j in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end='')
    if i != n-1 :
        print(',', end=' ')
print('>')