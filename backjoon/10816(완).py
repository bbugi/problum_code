# 숫자 카드 2 (실4)
# https://www.acmicpc.net/problem/10816

'''
Counter 함수 써보기

동일한 자료가 몇개인지 찾아주는 함수
''' 


# ========= 문제 풀이 (통과) - 728ms걸림 ==========

import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

c = Counter(n_list) 
# print(c)

print(*[c.get(i) if c.get(i) is not None else 0 for i in m_list])



# 문제풀이 1 ( 시간초과 발생 ) =============

# import sys
# input = sys.stdin.readline

# n_list = [0] * int(input())
# temp = list(map(int, input().split()))
# for i in range(len(n_list)):
#     n_list[i] = temp[i]

# m_list = [0] * int(input())
# temp = list(map(int, input().split()))
# for i in range(len(m_list)):
#     m_list[i] = temp[i]

# count_list = []
# for i in range(len(m_list)):
#     count_list.append(n_list.count(m_list[i]))

# print(*count_list)