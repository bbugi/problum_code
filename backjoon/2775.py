# 부녀회장이 될테야 (브1)
# https://www.acmicpc.net/problem/2775

'''
수학
구현
다이나믹 프로그래밍

'''


# ==== 문제 풀이 ===========

import sys
input = sys.stdin.readline

test_case = int(input())

for i in range(test_case): # 테스트 케이스만큼 입력 반복
    k = int(input()) # 층
    n = int(input()) # 호수
    
    # 1층의 3호에 살려면
    # 0층의 1호, 2호, 3호 (1+2+3)명이 들어와서 살아야 한다.
    
    # 2층의 3호에 살려면
    0층 : 1 , 2 , 3
    1층 : 1 , 3 , 6
    2층 : 2 , 7 , 16
    3층 : 4 , 16, 41
    
    
    