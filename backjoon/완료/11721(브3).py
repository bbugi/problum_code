# 열 개씩 끊어 출력하기 (브3)
# https://www.acmicpc.net/problem/11721

'''
구현, 문자열
'''

string = input()

for i in range(0,len(string),10) :
    print(string[i:i+10])