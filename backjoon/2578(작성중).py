# 빙고 (실4)
# https://www.acmicpc.net/problem/2578

# 이중배열


# ====== 첫번째 풀이 ===========

import sys
input = sys.stdin.readline

# 빙고판 생성
board = [list(map(int, input().split())) for _ in range(5)]

# mc가 부르는 숫자 리스트
bingo_nums = []
for _ in range(5):
    num = list(map(int, input().split()))
    bingo_nums.extend(num)  # extend() : 리스트 더하기

# print(bingo_nums)

# mc가 숫자 부른 횟수
cnt = 0
# 빙고판의 숫자와 mc가 부르는 숫자 같으면 빙고판 숫자 0으로 바꾸기
for i in range(25):
    for x in range(5):
        for y in range(5):
            if bingo_nums[i] == board[x][y]:
                board[x][y] = 0
                cnt += 1
print(board, cnt)


