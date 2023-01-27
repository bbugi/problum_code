# 연결 요소의 개수 (실2)
# https://www.acmicpc.net/problem/11724

'''
그래프 이론, 그래프 탐색
너비 우선 탐색
깊이 우선 탐색

'''

# ===== 문제 풀이 =====

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
result = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v) # 1과 연결된 숫자를 해당 인덱스 위치에 숫자를 더해주는 것
    graph[v].append(u)

print(graph)
print(visited)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        result += 1
        
print(result)

# for i in range(n):
#     u, v = map(int, input().split())
    