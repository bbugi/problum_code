# 대소문자 바꾸기 (브5)
# https://www.acmicpc.net/problem/2744

'''
대소문자 구분
isupper() : 대문자인지 확인
islower() : 소문자인지 확인
'''

# ===== 문제 풀이 =========

import sys
input = sys.stdin.readline

words = list(input().rstrip())
new = []

for word in words:
    if word.isupper() == True:
        word = word.lower()
    else:
        word = word.upper()
    new.append(word)
    
print(*new, sep='')