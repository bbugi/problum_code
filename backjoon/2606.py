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

# ============= 문제 풀이 ==============




# ==== 현우 풀이 =====

# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *


    def getdata():
        n = int(input())
        m = int(input())
        board = list(list(map(int, input().split())) for _ in range(m))
        return n, m, board

    n, m, board = getdata()
    gp = dict()
    for i in range(1,n+1) :
        gp[i] = list()
    for e in board :
        gp[e[0]].append(e[1])
        gp[e[1]].append(e[0])

    def bfs(gp, s) :
        need_visited, visited = deque(), deque()
        need_visited.append(s)
        while need_visited :
            node = need_visited.pop()
            if node not in visited :
                visited.append(node)
                need_visited.extend(gp[node])
        return len(visited)

    print(bfs(gp,1)-1)