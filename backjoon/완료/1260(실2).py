# DFS와 BFS(실2)
# https://www.acmicpc.net/problem/1260

'''
from collections import deque
import queue

# DFS와 BFS
지난번에 했던 바이러스랑 같은 문제니까 다시 한번 보면서 구글링과
지난 풀이 코드 공부하고 코드 한 줄씩 어떤 output을 뱉는지 보세요

'''

# ===== 문제 풀이 =====

# dfs 

# n : 정점의 개수
# m : 간선의 개수 (연결되는 수)
# v : 탐색을 시작할 수
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
# print(graph)
visited = [False] * (n+1)
# print(visited)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 갈 수 있는 수 중에 작은 수부터 진입해야 하므로 sort 해야함
for i in range(1, n+1):
    graph[i].sort()

# print(graph)
dfs_list = []
def dfs(graph, visited, visit_num):
    # 탐색 시작할 숫자부터 방문이 되니까 바로 visited에 
    visited[visit_num] = True
    # print(visit_num, end=" ")
    dfs_list.append(visit_num)

    # 그리고나서 탐색 시작한 숫자와 연결된 숫자들로 돌면서
    # 방문 확인하면서 탐색 마저하기
    for i in graph[visit_num]:
        if not visited[i]: # 방문한 적이 없다면
            dfs(graph, visited, i)

    return dfs_list
    

# bfs 
# dfs와 그래프는 동일한 모양임
from collections import deque

bfs_list = []
def bfs(graph, visited, visit_num):
    # 앞서 dfs에서 visited가 True로 채워져있기 때문에
    # 초기화 작업을 해줘야 함
    visited = [False] * (n+1)
    # 탐색할 숫자를 큐에 넣어주기
    queue = deque([visit_num])

    # 방문했다면 방문리스트를 True로 바꾸기
    visited[visit_num] = True

    while queue: # 큐가 비어있으면 False가 되면서 자동으로 while문이 멈춘다.
        # 큐에서 빠지는 숫자가 다음에 방문하는 숫자가 됨
        pop_v = queue.popleft()
        bfs_list.append(pop_v)

        for i in graph[pop_v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return bfs_list


print(*dfs(graph, visited, v))
print(*bfs(graph, visited, v))











# ===== 현우 풀이 =====
# from collections import deque, defaultdict

# n, m, v = map(int, input().split())
# board = list(list(map(int, input().split())) for _ in range(m))
# graph = defaultdict(list)

# def bfs(graph, v):
#     for e in board:
#         graph[e[0]].append(e[1])
#         graph[e[1]].append(e[0])
#     for i in range(1, n + 1):
#         graph[i].sort()
#     need_visited, visited = deque(), deque()
#     need_visited.append(v)
#     while need_visited:
#         node = need_visited.popleft()
#         if node not in visited:
#             visited.append(node)
#             need_visited.extend(graph[node])
#     return visited

# def dfs(graph, v):
#     for e in board:
#         graph[e[0]].append(e[1])
#         graph[e[1]].append(e[0])
#     for i in range(1, n + 1):
#         graph[i].sort(reverse=True)

#     need_visited, visited = deque(), deque()
#     need_visited.append(v)

#     while need_visited:
#         node = need_visited.pop()
#         if node not in visited:
#             visited.append(node)
#             need_visited.extend(graph[node])
#     return visited

# print(*dfs(graph, v))
# print(*bfs(graph, v))