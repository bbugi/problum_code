# 문자열 반복(브2)
# https://www.acmicpc.net/problem/2675

'''
구현, 문자열 문제
'''

# ==========문제 풀이==========

for _ in range(int(input())):
    r, s = input().split()

    r = int(r)
    s = list(s)

    for a in s:
        print(r*a, end='')
    print()
    
'''
맨 마지막에 print()를 빼먹으면
2
3 ABC
AAABBBCCC5 /HTP
/////HHHHHTTTTTPPPPP
이렇게 출력되어서 틀리는 것이고

마지막에 print를 넣어줘야
2
3 abc
aaabbbccc
5 /htp
/////hhhhhtttttppppp
이렇게 맞게 출력이 된다.
'''