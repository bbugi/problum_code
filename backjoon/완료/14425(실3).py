# 문자열 집합 (실3)
# https://www.acmicpc.net/problem/14425

'''
자료 구조
문자열
해시를 사용한 집합과 맵
트리를 사용한 집합과 맵
'''

# ====== 문제 풀이 - 단순 리스트를 통한 풀이 =====

n, m = map(int, input().split())

n_list = []
for _ in range(n):
    n_list.append(input())
    
# print(n_list)
cnt = 0
for _ in range(m):
    if input() in n_list:
        cnt += 1
print(cnt)
