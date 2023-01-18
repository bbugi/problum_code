# 스택 (실4)
# https://www.acmicpc.net/problem/10828

'''
스택 문제 풀어보기

스택
후입선출

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

'''

# ==== 문제 풀이 ======

import sys
input = sys.stdin.readline

n = int(input()) 
stack = []
for _ in range(n):
    input_ord = input().split() # 자동으로 리스트로 받아낸다.
    # print(input_ord)
    order = input_ord[0]
    # print(order)
    
    if order == 'push':
        stack.append(input_ord[1])
        
    elif order == 'pop':
        if len(stack) == 0:
            print(-1) # pop으로 뺀 요소에 대해서 프린트 해줘야하므로 맨 마지막 인덱스를 입력해줘야 한다.
        else:
            print(stack.pop(-1))
            
    elif order == 'size':
        print(len(stack))
        
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        
    

   
'''
=============== 실패 ==============
# 함수로 만들어서 해보기
# def stack(x, y):
#     s = []
#     if x == 'push':
#         return s.append(y)
#     elif x == 'pop':
#         if len(s) != 0:
#             return s.pop(-1)
#         else:
#             return -1
#     elif x == 'size':
#         return len(s)
    
#     elif x == 'empty':
#         if len(s) != 0:
#             return 0
#         else:
#             return 1
        
#     elif x == 'top':
#         if len(s) != 0:
#             return s[-1]
#         else:
#             return -1




=============== 실패 ==============
# 클래스 안에 메서드 만들기로 풀어야 하나?
class stack:
    def __init__(self): # 초기화 시키기
        self.s_list = []
        
    def push(self, y): # 출력 없음
        self.s_list.append(y)

    def pop(self): # pop된 숫자 출력해야함
        self.s_list.pop()
        if len(s_list) == 0:
            return -1
        else:
            return s_list.pop()
        
    def size(self):
        return self.len(s_list)
    
    def empty(self):
        if self.len(s_list) != 0:
            return 0
        else:
            return 1
        
    def top(self):
        if self.len(s_list) != 0:
            return s_list[-1]
        else:
            return -1

''' 