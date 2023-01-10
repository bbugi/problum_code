# 개수 세기(브5)
# https://www.acmicpc.net/problem/10807

#  ================ 문제 풀이 ===================

import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))
v = int(input())

def search_num(n, b, v):
    return(b.count(v))

print(search_num(n, b, v))
