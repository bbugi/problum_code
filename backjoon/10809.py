# 알파벳 찾기 (브5) - 브론즈 5문제인데 헤맸다.
# https://www.acmicpc.net/problem/10809


'''
a부터 z까지 리스트로 받기 위해서는 2가지 방식으로 리스트르
만들 수 있다.

1. chr(x)의 범위로 추가하기
lst = [chr(x) for x in range(97, 123)]
print( lst )

2. string 라이브러리 사용하여 추가하기 (아스키 코드 사용)
import string
lst = list( string.ascii_lowercase )
print( lst )
'''

# ===== 문제 풀기 ======

import string
lst = list( string.ascii_lowercase )
# print(lst)

s = list(input().lower())
# print(s)

count_lst = []

for i in lst:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')

