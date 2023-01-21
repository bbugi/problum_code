# 덱 (실4)
# https://www.acmicpc.net/problem/10866

'''
자료구조

덱 : deque
양방향 큐 자료구조
파이썬에서는 큐보다는 덱을 많이 사용한다

'''



# ======= 문제 풀이 ========

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

d = deque()
for i in range(n):
    x = input().split()
    order = x[0]

# def deque_manual(x):    
    if order == 'push_front':
        d.appendleft(x[1])
        
    elif order == 'push_back':
        d.append(x[1])
    
    elif order == 'pop_front':
        if len(d) != 0:
            print(d.popleft())
        else:
            print(-1)
    
    elif order== 'pop_back':
        if len(d) != 0:
            print(d.pop())
        else:
            print(-1)
    
    elif order == 'size':
        print(len(d))
        
    elif order == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
        
    elif order == 'front':
        if len(d) != 0:
            print(d[0])
        else:
            print(-1)
    
    elif order == 'back':
        if len(d) != 0:
            print(d[-1])
        else:
            print(-1)
    