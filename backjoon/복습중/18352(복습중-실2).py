# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

'''
그래프 이론, 그래프 탐색
너비 우선 탐색(bfs - deque 사용)
데이크스트라 - 최단거리를 찾는 알고리즘?

최단거리까지 같이 생각해야함.
'''

# ===== 문제 풀이 =====

# n = 1~n개까지의 도시가 존재
# m 개의 단방향 도로 존재 (연결 가능 개수)
# x = 탐색 시작 도시
# k = 최단 거리


# 입력받는 첫째 줄
# 도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발도시 번호 x

from collections import deque
import sys

input = sys.stdin.readline


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
# print(graph)
visited = [-1] * (n+1)
# print(visited)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a) # 양방향 그래프일때나 사용.. 해당 그래프는 단방향 그래프라서 이거때문에 출력 초과 일어남

# print(graph)

def bfs(start_num):
    queue = deque([start_num])
    visited[start_num] = 0

    while queue:
        pop_num = queue.popleft()
        
        for i in graph[pop_num]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[pop_num]+1

    return visited

# print(bfs(x))

if k not in bfs(x):
    print(-1)

# 출력시 오름차순으로 출력하라는 조건이 존재해서 ans에 넣어서
# 오름차순 정렬해줬는데, 없이 print해도 통과는 됨.

else:
    # ans = []
    for i in range(len(bfs(x))):
        # print(i)
        # print(bfs(x))
        # print(bfs(x)[i])
        if bfs(x)[i] == k:
            print(i)
            # ans.append(i)

    # print(*sorted(ans), sep='\n')
