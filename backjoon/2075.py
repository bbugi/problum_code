# N번째 큰 수 (실2)
# https://www.acmicpc.net/problem/2075

'''
자료구조, 정렬, 우선순위 큐
'''


import sys
input = sys.stdin.readline

n = int(input())


def check_num(check_arr):
    ans = [0] * n
    print(ck_arr)
    print(max(ans), min(ans))
    
    # print('함수에 n들어오는지 확인', n)
    idx = 0

    

for i in range(n):
    ck_arr = list(map(int, input().split()))
    ck_arr.sort(reverse=True)
    # print(ck_arr)
    check_num(ck_arr)


    























# ====== 시간초과, 메모리초과 >> 근데 틀렸을듯 =====

# import sys

# def check_num(check_num):
#     # print('함수에 n들어오는지 확인', n)
#     global ans
#     idx = 0
#     while idx < n :
#         ans = ans[:n]
#         print(ans)
#         # print('idx 값 확인', idx)
#         # print('ans[idx]값 확인',ans[idx])
#         if ans[idx] > check_num :
#             # print('if문 진입 확인')
#             idx += 1
#             # print(idx)

#         else :
#             # print('else문 진입 확인')
#             # print('else:::::',idx)
#             ans.insert(idx,check_num)
#             break

# input = sys.stdin.readline

# n = int(input())

# ans = [0] * n

# # print(ans)

# for i in range(n) :
#     check = list(map(int, input().split()))
#     # print('체크할 숫자 리스트 확인',check)
#     for c in check:
#         # print('체크할 숫자 확인',c)
#         check_num(c)
#     # print(ans[:n])
# print(ans[n-1])
















# import sys
# from collections import deque
# input = sys.stdin.readline

# def merge_sort(array) :
#     if len(array) < 2:
#         return array
#     mid = len(array)//2
#     left = merge_sort(array[:mid])
#     right = merge_sort(array[mid:])
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right) :
#         if left[i] <= right[j] :
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     if i == len(left) :
#         result += right[j:]
#     else:
#         result += left[i:]

#     return result


# n = int(input())
# board = [] 
# # ans = deque([0] * n)
# # print(ans)
# for i in range(n) :
#     board.extend(list(map(int, input().split())))
#     b2 = merge_sort(board)
# # print(board)


# # print(b2)
# print(b2[-n])

#     # board = list(map(int, input().split()))
#     # print(board)

#     # sort_list(board)
#     # print(board)










####### 일반적인 sorted 함수 사용한 풀이 >>> 메모리초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# board =[]

# for i in range(n):
#     board.extend(list(map(int, input().split())))
# # print(board)
    
# # board.sort(reverse=True)
# board = sorted(board, reverse=True)

# print(board[4])