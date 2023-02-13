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

def binary_search(n_list, search_value):
    first, last = 0, n-1

    while first <= last:
        mid = (first+last) // 2

        if n_list[mid] == search_value:
            return True

        if n_list[mid] > search_value:
            last = mid - 1

        else:
            first = mid + 1


# 테스트 케이스 t
t = int(input())

for _ in range(t):
# 수첩 1에 적어놓은 정수의 개수 n , 적힌 정수들
    n = int(input())
    book1 = list(map(int, input().split()))
    book1.sort()

    # 수첩 2에 적어놓은 정수의 개수 m , 적힌 정수들
    m = int(input())
    book2 = list(map(int, input().split()))

    # print(book1, book2)

    for i in range(m):
        if binary_search(book1, book2[i]) == True:
            print(1)
        else:
            print(0)
