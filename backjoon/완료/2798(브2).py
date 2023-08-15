# 블랙잭 (브2)
# https://www.acmicpc.net/problem/2798

'''
브루트포스 알고리즘
---
콤비네이션(조합) 사용하여 풀이함
'''

# n : 카드 개수 / m : 딜러가 부르는 수
# 카드는 3장 고르고, 딜러가 부르는 수 m을 넘지 않으면서 
# 최대한 가까워야 함

from itertools import combinations
n, m = map(int, input().split())

numbers = list(map(int, input().split()))

ans = 0

check_list = list(combinations(numbers, 3))

for i in range(len(check_list)) :
    check_sum = sum(check_list[i])
    if m >= check_sum > ans :
        ans = check_sum
print(ans)

# print(list(combinations(numbers, 3)))
# print(len(list(combinations(numbers, 3))))

