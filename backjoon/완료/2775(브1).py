# 부녀회장이 될테야 (브1)
# https://www.acmicpc.net/problem/2775

'''
수학
구현
다이나믹 프로그래밍

'''

# ==== 실제 문제 풀이 ===========

import sys
input = sys.stdin.readline

test_case = int(input())

for i in range(test_case): # 테스트 케이스만큼 입력 반복
    k = int(input()) # 층
    n = int(input()) # 호수
    
    # 아파트 층별 1호 거주민 수 = 항상 1명이므로 배열 생성을 1로 생성
    apt = [[1] * n for _ in range(k+1)]
    # print(apt)

    # 아파트 0층의 거주민 수
    apt[0] = [i for i in range(1, n+1)]
    # print(apt)



    def sum_kn(floor, ho):
        sum_ho = 0
        for i in range(ho+1):
            sum_ho += apt[floor-1][i]
        # print(sum_ho)
        return sum_ho
            
    # # 아파트 k층 n호 거주민 수 = k-1층의 1호~n호 까지의 거주민 수 합
    for i in range(1, k+1):
        for j in range(1,n):
            apt[i][j] = sum_kn(i,j)
    # print(apt)

    print(apt[k][n-1])





# ====== 문제 더 어렵게 해석해서 푼 식 
# (k층 n호에 살려면 그 아래의 모든 층을 더해야 한다고 해석) ==========


# import sys
# input = sys.stdin.readline

# test_case = int(input())

# for i in range(test_case): # 테스트 케이스만큼 입력 반복
#     k = int(input()) # 층
#     n = int(input()) # 호수



# # 배열 만들기

#     apt = [[0] * n for _ in range(k+1)] # 0층부터 k층까지 나와야 하므로 k+1범위
#     # print(apt)
        
#     # apt[0] = [1, 2, 3, 4]
#     # print(apt)
        
#     apt[0] = [i for i in range(1,n+1)] # apt[0] = [1, 2, 3, 4]
#     # print(apt)

#     # k층 1호는 2**k-1명이 산다
#     for i in range(1,k+1): # 인덱스범위를 k+1까지 잡아줘야 k까지 출력됨
#         apt[i][0] = 2**(i-1)

#     # print(apt)

#     # k층 n호는 (k층n-1호의 거주민 수) + (k-1층까지의 n호 거주민수의 합)
#     # apt[0][n] + apt[1][n] + apt[k-1][n]
#     def sum_kn(floor, ho):
#         sum_n = 0
#         for i in range(floor): # 0부터 k-1까지 범위
#             sum_n += apt[i][ho]
#         # print(sum_n) 
#         return sum_n    # for문 바깥에서 합쳐진 상태로 return 되도록 위치 잘 맞추기
            

#     # apt[k][n] = apt[k][n-1] + apt[0~k-1][n]
#     for i in range(1, k+1):
#         for j in range(1, n):
#             # apt의 1층의 2호는 
#             apt[i][j] = apt[i][j-1] + sum_kn(i,j)
#     print(apt)


#     print(apt[k][n-1])




