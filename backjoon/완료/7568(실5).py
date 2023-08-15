# 덩치 (실5)
# https://www.acmicpc.net/problem/7568

'''
구현, 브루트포스 알고리즘
'''

n = int(input())
wh = list()
d = {}

for i in range(n):
    wh.append(tuple(map(int, input().split())))

for i in range(n):
    d[i] = 1
    for j in range(n):
        if i == j :
            pass
        else:
            if (wh[i][0] < wh[j][0]) and (wh[i][1] < wh[j][1]) :
                # print(i,j, wh[i][0],wh[i][1], wh[j][0],wh[j][1])
                d[i] += 1

print(*d.values())


# for i in range(n-1):
#     # print('원본', wh)
#     print(i)
#     if wh[i][0] > wh[i+1][0] and wh[i][1] > wh[i+1][1] :
#         print(wh[i][0])
#         print(wh[i][1])

# print(d)

