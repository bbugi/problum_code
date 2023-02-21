# 미로 탐색 (실1)
# https://www.acmicpc.net/problem/2178

'''
그래프 이론, 그래프 탐색, 너비 우선 탐색

너비 우선 탐색(BFS)
깊이 우선 탐색(DFS)

'''

# ===== 문제 풀이 =====

'''
DFS 말고도 거리까지 저장을 해야 함

리스트에 담은 다음에
BFS 함수 안에서 좌우상하로 갈수 있는지 확인
1인지 확인, VISITED 한 곳인지 확인
갈 수 있으면 원래 값에 1을 더해주는 식으로 진행





백트래킹으로도 풀 수 있을 것 같은데..
경로를 계산할때는 백트래킹을 사용

거리를 계산하는 거에는 백트래킹은 아니다..?

'''



# ==== 현우 코드 =====

# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque

    def getdata():
        n, m = map(int,input().split())
        board = list(list(map(int, input().rstrip())) for _ in range(n))
        return n, m, board

    n, m, board = getdata()
    # 방문해야 할 곳(리스트), 방문한 곳 (딕셔너리로 줌)
    # 딕셔너리의 키 값을 (0,0)으로 미로의 위치 좌표를 
    # 
    need_visited, visited = deque(), dict()
    need_visited.append([0,0])
    visited[0,0] = 1
    while need_visited :
        nxt = need_visited.popleft()
        nx, ny = nxt[0], nxt[1]
        if nx == n-1 and ny == m :
            break
        if 0<=nx-1 and board[nx-1][ny] == 1 and (nx-1, ny) not in visited :
            need_visited.append([nx-1,ny])
            visited[nx-1, ny] = visited[nx, ny] + 1
        if 0<=ny-1 and board[nx][ny-1] == 1 and (nx, ny-1) not in visited :
            need_visited.append([nx,ny-1])
            visited[nx, ny-1] = visited[nx, ny] + 1
        if nx+1<n and board[nx+1][ny] == 1 and (nx+1, ny) not in visited :
            need_visited.append([nx+1,ny])
            visited[nx+1, ny] = visited[nx, ny] + 1
        if ny+1<m and board[nx][ny+1] == 1 and (nx, ny+1) not in visited :
            need_visited.append([nx,ny+1])
            visited[nx, ny+1] = visited[nx, ny] + 1
    print(visited[n-1, m-1])