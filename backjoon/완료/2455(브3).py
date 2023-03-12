# 지능형 기차 (브3)
# https://www.acmicpc.net/problem/2455

'''
수학, 구현, 사칙연산

'''

# ===== 문제 풀이 =====

n_list = []
n = 0
for i in range(4):
    d, u = map(int, input().split())
    n -= d
    n += u
    n_list.append(n)

print(max(n_list))