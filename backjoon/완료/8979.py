# 올림픽 (실5)
# https://www.acmicpc.net/problem/8979

'''
구현, 정렬 문제

'''


# ===== 문제 풀이 =====

import sys
input = sys.stdin.readline


n, k = map(int, input().split())

oly = []
for i in range(n):
    # 국가, 금, 은, 동
    oly.append(list(map(int, input().split())))   
# print(oly)

oly.sort(key= lambda x : (x[1], x[2], x[3]), reverse=True)
# print(oly)

# 여기 밑에 부분은 코드는 짰으나 결과가 나오지 않아서 블로그를 참조함

for i in range(n):
    if oly[i][0] == k: 
        index = i

for i in range(n):
    if oly[index][1:] == oly[i][1:]:
        print(i + 1) 
        break # 그 다음 등수가 나오지 않게끔 break 걸어주는 것 # 원래는 2, 3이 같이 나오는데,,,
        

# =============================