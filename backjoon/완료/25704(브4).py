# 출석 이벤트 (브4)
# https://www.acmicpc.net/problem/25704

'''
수학, 구현, 사칙연산 문제
'''

n = int(input())
p = int(input())


# 할인 쿠폰
coupon = [0, 5, 10, 15, 20]
discount = [0, 500, int(p*0.1), 2000, int(p*0.25)]
# 5, 10, 15, 20 개 이상 일때 할인 가능

# 할인 받고나서 지불해야하는 최소 금액 구하기
# 할인금액이 최대인 것을 적용하면 됨

price = []
for i in range(len(discount)):
    if coupon[i] <= n:
        price.append(p-discount[i])

if min(price) < 0:
    print(0)
else:
    print(min(price))


        


