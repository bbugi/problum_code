# 바이러스 (실3)
# https://www.acmicpc.net/problem/2606

'''
그래프 이론과 탐색에 관련한 문제입니다
처음보면 굉장히 생소하고 감이 안올거에요
그래프를 구성하는 방법은 여러가지가 있는데 저는 주로 dictionary 자료형을 사용해요
dictionary나 이중배열 등을 사용하여 index를 vertex로, value를 index와 이어진 vertex로 사용해서
edge도 정보를 담으면 돼요
탐색의 경우 고민하다 잘 안되면 dfs와 bfs를 검색하여 알고리즘 흐름을 느껴보세요

'''

# ===== 문제 풀이 =====

import sys
input = sys.stdin.readline

# 깊이 우선 탐색(DFS) 로 풀어보기
# DFS : 스택 사용 , 스택에 담는 순서가 중요, 방문 순서대로 스택에 담는다. 스택은 list로 표현 ( 후입 선출 ), 재귀로 사용 가능??


def dfs(start):
    visited[start] = 1
    route.append(start)
    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)


coms = int(input())
networks = int(input())

visited = [0] * coms
print(visited)



# route = []
# arr = []

# dfs(1)
# print(route)


# visited[1] = 1
# route.append(1)
# for i in arr[1]:
#     if visited[1] == 0:
#         dfs(i)



















# # dfs : 스택(리스트)
# n, m, k = map(int, input().split())

# graph = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# result = 0

# for i in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v) # 1과 연결된 숫자를 해당 인덱스 위치에 숫자를 더해주는 것
#     graph[v].append(u)

# # print(graph)
# # print(visited)

# def dfs(v):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)
            
# for i in range(1, n+1):
#     if not visited[i]:
#         dfs(i)
        

        
# print(result)



# bfs : 큐(덱)
from collections import deque

# ===== 현우 풀이 =====

# # coding = utf-8

# if __name__ == '__main__':
#     import sys

#     input = sys.stdin.readline
#     from collections import deque
#     from itertools import *


#     def getdata():
#         n = int(input())
#         m = int(input())
#         board = list(list(map(int, input().split())) for _ in range(m))
#         return n, m, board

#     n, m, board = getdata()
#     gp = dict()
#     for i in range(1,n+1) :
#         gp[i] = list()
#     for e in board :
#         gp[e[0]].append(e[1])
#         gp[e[1]].append(e[0])

#     def bfs(gp, s) :
#         need_visited, visited = deque(), deque()
#         need_visited.append(s)
#         while need_visited :
#             node = need_visited.pop()
#             if node not in visited :
#                 visited.append(node)
#                 need_visited.extend(gp[node])
#         return len(visited)

#     print(bfs(gp,1)-1)