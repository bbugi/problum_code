# 윷놀이 (브3)
# https://www.acmicpc.net/problem/2490

'''
구현
'''


# ====== 문제 풀이 ============

for _ in range(3):
    lst = list(map(int, input().split()))
    # print(lst)
    if lst.count(0) == 1:
        print('A')
    elif lst.count(0) == 2:
        print('B')
    elif lst.count(0) == 3:
        print('C')
    elif lst.count(0) == 4:
        print('D')
    else:
        print('E')