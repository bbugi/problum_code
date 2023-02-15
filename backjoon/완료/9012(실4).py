# 괄호(실4)
# https://www.acmicpc.net/problem/9012

'''
자료구조, 문자열, 스택(리스트 사용) 문제
'''

# readline 으로 입력받으면 개행문자 \n이 같이와서 답이 틀린걸로 나타난다.
# 리스트 안이 비어있어야 yes 출력되는데 개행문자가 들어있어
# 리스트 안에 인수가 있는 것으로 받아 no를 출력하기 때문

# int로 받으면 개행문자를 안받는데, 
# 아래에 vps는 input 문자로 받으면서 개행문자를 받은 것이므로 .rstrip() 으로 개행문자 제거하기

import sys
input = sys.stdin.readline


# 테스트 케이스 t
t = int(input())

for i in range(t):
    vps = input().rstrip()
    lst = []
    for v in vps:
        # print(v)
        lst.append(v)
        if len(lst) >= 2:
            if lst[-2] == "(" and lst[-1] == ")":
                lst.pop()
                lst.pop()

    if not lst:
        print("YES")
    else:
        # print(lst)
        print("NO")
