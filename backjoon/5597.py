# 과제 안 내신 분..? (브5)
# https://www.acmicpc.net/problem/5597

# ========= 문제 풀이 ==========

# 1번부터 30번까지 출석번호 존재
# 입력은 28명만 제출
# 제출안한 2명의 출석번호를 작은 순서로 2줄로 출력하라

import sys
input = sys.stdin.readline

a = list(range(1,31))
# print(a)
for _ in range(28):
    n = int(input())
    a.remove(n)
    # print(n, a)
print(*a, sep='\n')
print(a, sep='\n')


# =========== 참조 =============

# # *리스트 : 어퍼스트로피 사용
# a = [1,2,3,4,5]
# print('print a:',a, sep='\n')
# print('print(*a) : ', *a, sep='\n')