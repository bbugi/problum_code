#  아스키 코드 (브5)
# https://www.acmicpc.net/problem/11654

'''
파이썬 
문자를 아스키코드로 변환함수 : ord('문자')

아스키코드를 문자로 변환함수 : chr('아스키 코드')
'''
# ======== 문제 해결 =========

import sys
input = sys.stdin.readline

print(ord(input().rstrip()))
