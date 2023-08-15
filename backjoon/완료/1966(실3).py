# 프린터 큐 (실3)
# https://www.acmicpc.net/problem/1966

'''
구현, 자료구조, 큐, 시뮬레이션
'''

from collections import deque
# queue = deque()
# imp_q = deque() # 큰 숫자가 중요도 높은 것

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    pop_num = []

    queue = deque([i+1 for i in range(n)])
    find_num = queue[m]
    # 두번째 줄 = n개의 문서의 중요도가 차례로 주어짐 (중요도가 같은 문서 여러개 존재 有)
    imp_q = deque(map(int, input().split()))

    while True:
        if len(imp_q) == 0 :
            break
    
        max_idx = imp_q.index(max(imp_q))
        # print(max_idx)

        if max_idx != 0:
            queue.rotate(-1)
            imp_q.rotate(-1)
            # print('queue1:', queue)
            # print('imp_q1:', imp_q)
            continue

        elif max_idx == 0:
            pop_num.append(queue.popleft())
            imp_q.popleft()
            # print('queue2:', queue)
            # print('imp_q2:', imp_q)
            continue

    for num in pop_num :
        if find_num == num :
            print(pop_num.index(num) + 1)



    