# 참외밭 (실2)
# https://www.acmicpc.net/problem/2477

'''




'''

# ========= 문제 풀이 ============



import sys
input = sys.stdin.readline

n = int(input())

max_h = 0
max_v = 0
max_h_index = 0
max_v_index = 0

x_list = []
for i in range(6):
    temp = list(map(int, input().split()))
    x_list.append(temp)
print(x_list)

for i in range(6):
    if x_list[i][1]


# for i in range(1, 5):
#     if x_list.count(i) == 1:
#         # print(i)
        



















# x_list = []
# y_list = []
# for i in range(6):
#     x, y = map(int, input().split())
#     x_list.append(x)
#     y_list.append(y)
    
# # for i in range(1, 5):
#     # print(f'{i}:', x_list.count(i)
# h_max = []
# v_max = []
# for i in range(4):
#     if x_list[i] ==  1 or x_list[i] == 2:
#         h_max.append(y_list[i])

#     elif x_list[i] ==  3 or x_list[i] == 4:
#         v_max.append(y_list[i])
        
# print(max(h_max))
# print(max(v_max))

# if max(h_max) == 

# max 길이에 인접하지 않은 길이를 뺄 넓이로 사용하면 된다.






# 리스트에 중복되는 값이 있을때 다중 index 값 추출
