# N과 M (1) (실3)
# https://www.acmicpc.net/problem/15649

'''
백트래킹

백트래킹을 사용한 순열과 조합 풀이에 사용하는 itertools

iterable에서 원소 개수가 r인 조합 뽑기 (중복 없음)
입력된 반복가능한 객체의 순서에 따라 사전식 순서로 방출
입력값이 정렬되어 있으면 조합 튜플이 정렬된 순서로 생성됨

itertools.permutations(리스트, 개수) : 순열
itertools.combinations(리스트, 개수) : 조합

* '구분자'.join(리스트)
리스트가 숫자로 되어있으면 join 명령어가 안먹히므로
str(문자형)으로 바꿔주어야 한다.

'''


# ====== 문제 풀이 =====

import itertools
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
    
lst = []
for i in range(1, n+1):
    lst.append(i)
    
# print(lst)
c = itertools.permutations(lst, m)
for num in c:
    num = ' '.join(map(str, num))
    print(num)

# print((list(c)), sep='\n')

