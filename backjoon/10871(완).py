# x보다 작은 수(브5)
# https://www.acmicpc.net/problem/10871

#  ========= 문제 풀이 ==========

import sys
input = sys.stdin.readline

n, x= map(int, input().split())
v = list(map(int, input().split()))
        
def small_x(n, x, v):
    for i in range(len(v)):
        if x > v[i]:
            print(v[i], end=' ')
            
small_x(n,x,v)