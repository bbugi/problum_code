# 수 찾기 (실4)
# https://www.acmicpc.net/problem/1920

'''
자료구조
정렬
이분 탐색

'''

# ==== 문제 풀이 - 이분탐색(binary_search) 사용하기 ====
# 참조 블로그 : https://brownbears.tistory.com/565

import sys
input = sys.stdin.readline

def binary_search(n_list, search_value): 
    first, last = 0, n-1
    
    while first <= last:
        mid = (first + last) // 2

        if n_list[mid] == search_value:
            return True
        
        if n_list[mid] > search_value:
            last = mid - 1
        else:
            first = mid + 1

            
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
# print(n_list)

m = int(input())
m_list = list(map(int, input().split()))

for i in range(m):
    # print(m_list[i])
    if binary_search(n_list, m_list[i]) == True:
        print(1)
    else:
        print(0)
        








# ==== 문제 풀이 - 이분탐색 코드 안써서 시간초과 발생 =======

# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))
# # print(a)

# m = int(input())
# b = list(map(int, input().split()))
# # print(b)
# b_check = [0] * m

# for i in range(len(b)):
#     for j in range(len(a)):
#         if b[i] == a[j]:
#             b_check[i] = 1

# print(*b_check, sep='\n')