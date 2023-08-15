# 등수 매기기 (실3)
# https://www.acmicpc.net/problem/2012

'''
그리디 알고리즘, 정렬

일반 sort / sorted로 풀었을때는 백준에서 시간초과가 발생
그런데 import sys 를 활용하여
input값을 변경해주니
동일한 코드라도 성공이 떴다.
readline을 통해 입력값을 받을 경우
속도의 영향이 큰 듯?하다
'''

import sys

input = sys.stdin.readline

n = int(input())
dis_sati = 0
pred_rank = []

for i in range(n):
    pred_rank.append(int(input()))

# pred_rank.sort()
pred_rank = sorted(pred_rank)

for idx, rank in enumerate(pred_rank):
    dis_sati += abs(rank - (idx+1))
print(dis_sati)
