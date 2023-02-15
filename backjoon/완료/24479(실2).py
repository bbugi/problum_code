# 알고리즘 수업 - 깊이 우선 탐색 1 (실2)
# https://www.acmicpc.net/problem/24479

'''
깊이 우선 탐색 (dfs) - 스택 사용 - 재귀함수 사용
'''

# n : 정점의 개수
# m : 연결 개수
# r : 시작점
# 양방향 간선이다. 길이는 1이다

import sys
input = sys.stdin.readline

# 재귀의 깊이를 제한하는 모듈
sys.setrecursionlimit(10**7)


n, m, r = map(int, input().split())

graph = [[] for i in range(n+1)]
# print(graph)
visited = [0] * (n+1)
# print(visited)

# 그래프 먼저 채우기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 정점은 오름차순으로 방문한다.
for g in graph:
    g.sort()


# 해당 정점에 방문한 숫자가 중요한 것..
# 그럴려면 방문할때마다 카운트를 증가?
cnt = 1
def dfs(graph, visit_num, visited):
    # 함수 밖에 지정한 cnt =1 이라는 값을 사용하기 위해
    # global로 변수 등록해줘야 함.
    global cnt
    
    # 방문확인할 때 False-> True로 바꾸는게 아니라
    # 방문한 횟수가 되는 cnt를 입력해준다.
    visited[visit_num] = cnt
    
    for i in graph[visit_num]: # 그래프의 해당 숫자에서 방문 가능한 값들을 i로 돌림
        if visited[i] == 0:# 해당 숫자가 방문한적 없다면
            cnt += 1
            dfs(graph,i, visited) # dfs 재귀함수로 i를 방문하는걸로 진행

# 함수 실행 -> 함수 실행하면서 visited 리스트가 채워진다.
dfs(graph, r, visited)

for i in range(n+1):
    if i != 0:
        print(visited[i])
        # dfs 함수를 돌면서 만든 visited 리스트의 값을 출력
        # 해당 인덱스에 대한 방문 순서가 입력되어 있으므로
        # 출력되는 값 자체가 해당 정점에 몇번째에 방문했는지 알 수 있음
        

