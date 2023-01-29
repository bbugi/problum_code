# 거스름돈 (브2)
# https://www.acmicpc.net/problem/5585

# 그리디 알고리즘

# ===== 문제 풀이 =====

import sys
input = sys.stdin.readline


# ==== 그리디 알고리즘 사용해보기 ====

money = [500, 100, 50, 10, 5, 1]

n = 1000 - int(input())
coin = 0
for i in money:
    print('n // i: ', n // i)
    print('n % i: ', n % i)    
    coin += n // i # 동전으로 나눈 몫 (받은 동전의 개수)
    n %= i # 나머지 (동전을 받고 난 다음 남은 잔액)

print(coin)



# ===== 잔돈 구하기 1번 풀이 (풀어서 쓰기) ======
# coin = 0
# charge = 1000 - int(input())

# while charge > 0:
#     coin += 1
#     if charge >= 500:
#         charge = charge - 500
#         money = charge
#         continue

#     elif charge >= 100:
#         charge = charge - 100
#         money = charge
#         continue

#     elif charge >= 50:
#         charge = charge - 50
#         money = charge
#         continue

#     elif charge >= 10:
#         charge = charge - 10
#         money = charge
#         continue

#     elif charge >= 5:
#         charge = charge - 5
#         money = charge
#         continue

#     elif charge >= 1:
#         charge = charge - 1
#         money = charge
#         continue

# print(coin)