# 한조서열정리하고옴ㅋㅋ (브1)
# https://www.acmicpc.net/problem/14659

n = int(input())
n_list = list(map(int, input().split()))
cnt = 0

i = 0
tmp = 0
for i in range(n-1):
    for j in range(i, n) :
        if n_list[i] > n_list[j] :
            tmp += 1
        else:
            i = j
            print(tmp)
            break
        
            





# ======== 시간초과 문제 ============

# n = int(input())

# n_list = list(map(int, input().split()))

# cnt = 0

# for i in range(n-1):
#     tmp = 0 
#     # print(i, '언제들어와')
#     for j in range(i, n):
#         # print(i,j, '언제들어와')
#         if i == j:
#             pass
#         elif n_list[i] > n_list[j] :
#             # print(i,j, '여기서 tmp 추가됨')
#             tmp += 1
#         else:
#             break
#         if cnt < tmp :
#             cnt = tmp

# print(cnt)