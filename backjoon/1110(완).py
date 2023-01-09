# 더하기 사이클

# def sum_cycle(n):
#     cycle_num = 0
#     ans = n
#     z = 0
#     while True:
#         if z == 0:
#             x = list(map(int, str(n).zfill(2)))
#             y = list(map(int, str(sum(x)).zfill(2)))
#             z = int(str(x[1]) + str(y[1])) # 새로운 n이 되어야 함
#             cycle_num += 1

#             continue
#         elif z == ans:
#             return cycle_num
#             break
#         else:
#             x = list(map(int, str(z).zfill(2)))
#             y = list(map(int, str(sum(x)).zfill(2)))
#             z = int(str(x[1]) + str(y[1]))
#             cycle_num += 1
#             continue

# n = int(input())
# print(sum_cycle(n))


# =============== 시간초과 안뜨게 다시 풀어보기 ==============

# 최종 제출 코드

import sys
input = sys.stdin.readline

n = int(input())
ans = n
num_cnt = 0
while True:
    if num_cnt == 0:
        n1 = n // 10 # 10의자리 수
        n2 = n % 10 # 1의 자리 수
        k = n1 + n2
        k1 = k // 10
        k2 = k % 10
        n = int(str(n2) + str(k2))
        num_cnt += 1
        continue
    elif n != ans:
        n1 = n // 10 # 10의자리 수
        n2 = n % 10 # 1의 자리 수
        n = n1 + n2
        k = n1 + n2
        k1 = k // 10
        k2 = k % 10
        n = int(str(n2) + str(k2))
        num_cnt += 1
        continue
    else:
        print(num_cnt)
        break


