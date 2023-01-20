# 카드1(실5)
# https://www.acmicpc.net/problem/2161


'''
자료구조 - 큐(queue) 사용하기

'''
# ============ 문제 풀이 ==============

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q =  deque( i for i in range(1,n+1))
q_list = []

for i in range(n):
    # print(i)
    q_list.append(q.popleft())
    if len(q) != 0:
        q.append(q.popleft())
    else:
        pass
    # print(q)
    # print(q_list)
    # print(len(q))
print(*q_list)

    # q_list.append(q.popleft())
    # q.append(q.popleft())
# q_list.append(q.popleft())
# q.append(q.popleft())

# print(q_list)


