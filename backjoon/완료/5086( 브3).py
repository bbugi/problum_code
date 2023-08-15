# 배수와 약수 (브3)
# https://www.acmicpc.net/problem/5086

'''
수학, 사칙연산
'''

while True:
    a, b = map(int, input().split())

    if a == b == 0:
        break

    elif b % a == 0 :
        print('factor')

    elif a % b == 0:
        print('multiple')

    else: 
        print('neither')
