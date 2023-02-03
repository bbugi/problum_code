# 암기왕 (실4)
# https://www.acmicpc.net/problem/2776

'''
자료구조, 정렬
이분탐색
해시를 이용한 집합과 맵 (딕셔너리 형태)
'''



# ===== 문제 풀이 - 이분탐색 통해서 풀어보기 =====

import sys
input = sys.stdin.readline

t = int(input())

n = int(input())
book1 = list(map(int, input().split()))

m = int(input())
book2 = list(map(int, input().split()))

print(book1, book2)
