# 상수 (브2)
# https://www.acmicpc.net/problem/2908

'''
수학, 구현 문제
'''

# ===== 문제 풀이 ===========

import sys
input = sys.stdin.readline

num1, num2 = input().split() # 입력값을 받을 때는 str으로 받았다가

num1 = int(num1[::-1]) # 진짜 비교해야 하는 값으로 바꿀때 int 형식으로 바꾸기
num2 = int(num2[::-1])

print(max(num1, num2))