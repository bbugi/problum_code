# 참외밭 (실2)
# https://www.acmicpc.net/problem/2477

'''


'''

# ===== 문제 풀이 ============
# deque를 활용해 원하는 모양이 나올때까지 rotate 시켜서 구하고 싶은 값 구하기

from collections import deque

k = int(input())

a_list = deque()
b_list = deque()
for i in range(6):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

# print(a_list)
# print(b_list)

# 원하는 규칙이 나올때까지 리스트 모양 바꾸기
while True:
    if a_list[0] == a_list[2] and a_list[1] == a_list[3]:
        small = (b_list[1] * b_list[2])
        big = (b_list[4] * b_list[5])
        break
    else:
        a_list.rotate(-1)
        b_list.rotate(-1)

# print(a_list)
# print(b_list)

# max1 = []
# for i in range(1,5):
#     if a_list.count(i) == 1:
#         # print(i) # 2, 4
#         max1.append(b_list[a_list.index(i)])
# # print(max1)

# big = max1[0] * max1[1]

print((big - small) * k)




# ======= 지섭오빠 풀이 ============
# 넓이를 이용해 푸는 방법
# 넓이를 모두 이용해서 곱하면 사각형이 6개가 나온다
# 와.. 이런 접근을...?

# n = int(input())
# lens = []
# for i in range(6):
#     lens.append(int(input().split()[1]))
# lens.append(lens[0])

# total, max_area = 0, 0
# for i in range(6):
#     total += lens[i] * lens[i+1]
#     if max_area < lens[i] * lens[i+1]:
#         max_area = lens[i] * lens[i+1]

# print(n * (total - 2 * max_area))













# ========= 문제 풀이 ============


# import sys
# input = sys.stdin.readline

# n = int(input())

# max_h = 0
# max_v = 0
# max_h_index = 0
# max_v_index = 0

# x_list = []
# for i in range(6):
#     temp = list(map(int, input().split()))
#     x_list.append(temp)
# print(x_list)

# for i in range(6):
#     if x_list[i][1]


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




'''
반례 확인하기

7
4 50
2 160
3 30
1 60
3 20
1 100

7
2 160
3 30
1 60
3 20
1 100
4 50

7
3 30
1 60
3 20
1 100
4 50
2 160

7
1 60
3 20
1 100
4 50
2 160
3 30

7
3 20
1 100
4 50
2 160
3 30
1 60

7
1 100
4 50
2 160
3 30
1 60
3 20



'''