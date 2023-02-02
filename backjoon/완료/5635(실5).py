# 생일 (실5)
# https://www.acmicpc.net/problem/5635

'''
문자열, 정렬, 구현문제
'''

# ======= 문제 풀이 =======

import sys
input = sys.stdin.readline

n = int(input())
info = []

# 이름 dd mm yyyy 순으로 입력
for i in range(n):
    info.append(input().split())
    info[i][1] = int(info[i][1])
    info[i][2] = int(info[i][2])
    info[i][3] = int(info[i][3])
    print(info)
# 나이가 가장 적은 사람 : 연도 > 월 > 일이 모두 큰 순서
# 리스트(문자열) 정렬 
info = sorted(info, key= lambda x : (x[3], x[2], x[1]))

print(info[-1][0], info[0][0], sep='\n')
