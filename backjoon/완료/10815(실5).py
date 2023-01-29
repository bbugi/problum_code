# 숫자 카드 (실5)
# https://www.acmicpc.net/problem/10815


'''
자료구조- 정렬, 이분 탐색

'''

# ==== 문제 풀이  ====
# 리스트 대신에 set을 이용해도 시간초과를 벗어날 수 있다??

import sys
input = sys.stdin.readline

n = int(input())
n_list = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))


for num in m_list:
    if num in n_list:
        print(1, end=' ')
    else:
        print(0, end=' ')



# ==== 문제 풀이 - 시간초과 발생 ====

# import sys
# input = sys.stdin.readline

# n = int(input())
# n_list = list(map(int, input().split()))

# m = int(input())
# m_list = list(map(int, input().split()))


# for num in m_list:
#     if num in n_list:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')