# 윷놀이 (브3)
# https://www.acmicpc.net/problem/2490

'''
구현

if 문을 나열할거면 딕셔너리의 키값으로 지정해도 된다.
해당 문제의 경우 1이면 A, 2이면 B 이런식으로...
그래서 이거는 딕셔너리로 dict = {1:'A', 2:'B', ...} 이렇게 한줄로 정의가능

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