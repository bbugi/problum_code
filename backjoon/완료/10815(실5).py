# 숫자 카드 (실5)
# https://www.acmicpc.net/problem/10815


'''
자료구조- 정렬, 이분 탐색

이분탐색 함수를 만들때 내부적으로 잘 바꿔야 하는 경우가 많다.
그래서 이분탐색 활용해서 다시 풀어볼 것

'''

# ==== 문제 풀이  ====
# 리스트 대신에 set을 이용해도 시간초과를 벗어날 수 있다??

import sys
input = sys.stdin.readline

n = int(input())
n_list = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))


for num in m_list:
    if num in n_list:
        print(1, end=' ')
    else:
        print(0, end=' ')



# ==== 문제 풀이 - 시간초과 발생 ====

# import sys
# input = sys.stdin.readline

# n = int(input())
# n_list = list(map(int, input().split()))

# m = int(input())
# m_list = list(map(int, input().split()))


# for num in m_list:
#     if num in n_list:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')




# === 현우 코드 ==== 
# # coding = utf-8

import sys
input = sys.stdin.readline

def binarysearch(ls, num):
    left = 0
    right = len(ls)-1
    while left <= right:
        mid = (left+right) // 2
        if ls[mid] == num:
            return 1
        elif ls[mid] < num:
            left = mid + 1
        else :
            right = mid - 1
    return 0

n = int(input())
num_list = list(map(int,input().split()))
num_list.sort()
print(num_list)
m = int(input())
call = list(map(int, input().split()))
for num in call:
    print(binarysearch(num_list, num), end=" ")