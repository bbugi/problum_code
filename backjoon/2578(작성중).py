# 빙고 (실4)
# https://www.acmicpc.net/problem/2578

# 이중배열


# ====== 첫번째 풀이 ===========

# import sys
# input = sys.stdin.readline

# board = [list(map(int, input().split())) for _ in range(5)]

# bingo_nums = []
# for _ in range(5):
#     num = list(map(int, input().split()))
#     bingo_nums.extend(num) 


# cnt = 0
# for i in range(25):
#     for x in range(5):
#         for y in range(5):
#             if bingo_nums[i] == board[x][y]:
#                 board[x][y] = 0
#                 cnt += 1

     
# print(cnt)


#  구현 시뮬















# ========== 조합이 안돼.... =============

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]

bingo_nums = []
for _ in range(5):
    num = list(map(int, input().split()))
    bingo_nums.extend(num) 


cnt = 0
count_bingo = 0
board_col = [[99] * 5 for i in range(5)]
bingo_left = []
bingo_right = []


# 함수를 만들어서 정리해보자
def bingo_row(board):
    
    
    
    for x in range(5):
        for y in range(5):
            board_col[x][y] = board[y][x]





for i in range(25):
    cnt += 1
    count_bingo = 0
    for x in range(5):
        for y in range(5):
            if bingo_nums[i] == board[x][y]:
                board[x][y] = 0
                

                        
                for board_row in board: # 가로 빙고 성공했을 때
                    # print(board_row)
                    if board_row.count(0) == 5:
                        count_bingo += 1   

                for col in board_col:
                    # print(col)
                    if col.count(0) == 5:
                        count_bingo += 1 

                for x in range(5):   
                    for y in range(5):         
                        if  x + y == 4:
                            bingo_right.append(board[x][y])
                            if bingo_right.count(0) == 5:
                                count_bingo += 1
                        if x == y:
                            bingo_left.append(board[x][y])
                            if bingo_left.count(0) == 5:
                                count_bingo += 1
     
if count_bingo >= 3:
    print(cnt)


# ============ 현우 코드 =============

# coding = utf-8

import sys
input = sys.stdin.readline

bn = 5
bingo = list(list(map(int,input().split())) for _ in range(bn))
call = list(list(map(int,input().split())) for _ in range(bn))
visited = list(list(False for _ in range(bn)) for _ in range(bn))

def printboard(board) :
    for row in board :
        print(row)


def erasenum(n, bingo, visited) :
    for i in range(bn) :
        for j in range(bn) :
            if bingo[i][j] == n :
                visited[i][j] = True
                return

def checkbingo(visited) :
    ch = 0
    # 가로 check
    for row in visited :
        if row.count(True) == bn :
            ch += 1
    # 세로 check
    for i in range(bn) :
        tmp = 0
        for j in range(bn) :
            if visited[j][i] == True :
                tmp += 1
        if tmp == bn :
            ch += 1
    # 좌상 우하 대각선 check
    tmp = 0
    for i in range(bn) :
        if visited[i][i] == True :
            tmp += 1
    if tmp == bn :
        ch += 1
    # 우상 좌하 대각선 check
    tmp = 0
    for i in range(bn):
        if visited[i][-i-1] == True:
            tmp += 1
    if tmp == bn:
        ch += 1

    return ch

def sol() :
    res = 0
    for row in call :
        for num in row :
            erasenum(num, bingo, visited)
            res += 1
            if checkbingo(visited) >= 3 :
                return res

print(sol())





        
# ====================================================

# print(cnt)

# if count_bingo <= 3:                       
#     for board_row in board: # 가로 빙고 성공했을 때
#         # print(board_row)
#         if board_row.count(0) == 5 :
#             count_bingo += 1   

#     for col in board_col:
#         # print(col)
#         if col.count(0) == 5:
#             count_bingo += 1 

#     for x in range(5):   
#         for y in range(5):         
#             if  x + y == 4:
#                 bingo_right.append(board[x][y])
#                 if bingo_right.count(0) == 5:
#                     count_bingo += 1
#             if x == y:
#                 bingo_left.append(board[x][y])
#                 if bingo_left.count(0) == 5:
#                     count_bingo += 1

# else:
#     print(cnt)
                        
                # check_row(board)
                # check_col(board_col)
# for board_row in board: # 가로 빙고 성공했을 때
#     # print(board_row)
#     if board_row.count(0) == 5 :
#         count_bingo += 1                

# for col in board_col:
#     print(col)
#     if col.count(0) == 5:
#         count_bingo += 1  
        
# for 

                        

                    





















# ============= 문제 풀이 과정 ===========
# import sys
# input = sys.stdin.readline

# # 빙고판 생성
# board = [list(map(int, input().split())) for _ in range(5)]
# # bingo = [[0]*5 for _ in range(5)]

# # mc가 부르는 숫자 리스트
# bingo_nums = []
# for _ in range(5):
#     num = list(map(int, input().split()))
#     bingo_nums.extend(num)  # extend() : 리스트 더하기

# # print(bingo_nums)

# # 빙고인지 확인하기

# # 가로빙고 x가 동일 
# # h_cnt = 0

#     # if x == i :
#     #     if board[x][y].count(0) == 5:
   
# # # 세로빙고 y가 동일
# # for i in range(5):
# #     if y == i:
   
# # d_bingo = 0 # 대각선빙고 x == y or (0,4)(1,3)(2,2)(3,1)(4,0)


# # mc가 숫자 부른 횟수
# cnt = 0
# # 빙고판의 숫자와 mc가 부르는 숫자 같으면 빙고판 숫자 0으로 바꾸기
# for i in range(25):
#     for x in range(5):
#         for y in range(5):
#             # print("i, x, y", i, x, y)
#             if bingo_nums[i] == board[x][y]:
#                 board[x][y] = 0
#                 cnt += 1

#             for i in range(5):
#                 if x == i :
#                     print(board[x][y])
#                     if sum(board[x]) == 0:
#                         h_cnt += 1
# print(h_cnt)

# print(h_bingo_cnt)
                    
                



