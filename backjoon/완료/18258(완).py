# 큐 2 (실4)
# https://www.acmicpc.net/problem/18258

# 시간제한 있는 문제 (3초)

'''
큐 문제 풀어보기

큐(queue)
선입선출
쌓이는 것은 뒤로만 쌓이고 빼는건 앞에서부터 뺀다.


(확인요망)빼고나서 인덱스가 당겨지지 않는다. 뺀 공간은 빈자리로 남겨둔다. (새롭게 채워넣지 않음)
문제를 풀때 가장 앞자리 인덱스가 0으로 된 것을 확인했다..


똑같은 큐 라면 덱을 사용해서 풀어도 되는지?

'''

# 1. 덱을 이용해서 풀어보기 ============

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()

for i in range(n):
    input_ord = input().split()
    order = input_ord[0]

    if order == 'push':
        d.append(input_ord[1])
        
    elif order == 'pop':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
            
    elif order == 'size':
        print(len(d))
        
    elif order == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0]) # deque의 경우도 앞의 값이 빠지면 인덱스가 0으로 되는걸...??
    elif order == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])            
            



