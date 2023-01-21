# 분산처리 (브2)
# https://www.acmicpc.net/problem/1009

'''
수학, 구현 문제

엑셀에서 1~10까지 제곱수를 확인
일정한 규칙 확인

[반복]      [a숫자]
1	        1
2 4 8 6	    2
3 9 7 1	    3
4 6	        4
5	        5
6	        6
7 9 3 1	    7
8 4 2 6	    8
9 1	        9
10	        10

'''

# ===== 문제 풀이 ==========

def com_num(a, b):    
    if a % 10 == 1 :
        print(1)

    elif a % 10 == 2 :
        if b % 4 == 1:
            print(2)
        elif b % 4 == 2:
            print(4)
        elif b % 4 == 3:
            print(8)
        elif b % 4 == 0:
            print(6)
            
    elif a % 10 == 3 :
        if b % 4 == 1:
            print(3)
        elif b % 4 == 2:
            print(9)
        elif b % 4 == 3:
            print(7)
        elif b % 4 == 0:
            print(1)
            
    elif a % 10 == 4 :
        if b % 2 == 1:
            print(4)
        elif b % 2 == 0:
            print(6)
            
    elif a % 10 == 5 :
        print(5)
        
    elif a % 10 == 6 :
        print(6)
        
    elif a % 10 == 7 :
        if b % 4 == 1:
            print(7)
        elif b % 4 == 2:
            print(9)
        elif b % 4 == 3:
            print(3)
        elif b % 4 == 0:
            print(1)
            
    elif a % 10 == 8 :
        if b % 4 == 1:
            print(8)
        elif b % 4 == 2:
            print(4)
        elif b % 4 == 3:
            print(2)
        elif b % 4 == 0:
            print(6)
            
    elif a % 10 == 9 :
        if b % 2 == 1:
            print(9)
        elif b % 2 == 0:
            print(1)
            
    elif a % 10 == 0 :
        print(10)



t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    com_num(a, b)









# ===== 첫번째 문제풀이 - 시간초과 발생 ===========
# t = int(input())

# for i in range(t):
#     a, b = map(int, input().split())
#     if a == 10:
#         print(10)
#     else:
#         print((a**b) % 10)
        