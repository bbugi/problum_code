# 방 배정 (브2)
# https://www.acmicpc.net/problem/13300


# -----------------------

n, k = map(int, input().split())

# s : 성별 / y : 학년
wy_list = [0] * 7
my_list = [0] * 7
# print(y_list)
for i in range(n):
    s, y = map(int, input().split())
    if s == 0: # 여학생인 경우
        wy_list[y] += 1
    else:
        my_list[y] += 1

# print(wy_list)
# print(my_list)

room = 0
for i in range(1,7):
    room += wy_list[i]//k
    if wy_list[i]%k > 0:
        room += 1
    
    room += my_list[i]//k
    if my_list[i]%k > 0:
        room += 1

print(room)
    

    # if 0 < wy_list[i] <= k:
    #     room += 1
    # elif wy_list[i] > k:
    #     room += 2

    # if 0 < my_list[i] <= k:
    #     room += 1
    # elif my_list[i] > k:
    #     room += 2
