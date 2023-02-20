# 차량 번호판 1 (브1)
# https://www.acmicpc.net/problem/16968

'''
수학, 조합론
'''
lst = list(input())

cnt = 0
if lst[0] == 'c':
    cnt = 26
else:
    cnt = 10
    
for i in range(1, len(lst)):
    if lst[i] == 'c':
        if lst[i] == lst[i-1]:
            cnt *= 25
        else:
            cnt *= 26
    else:
        if lst[i] == lst[i-1]:
            cnt *= 9
        else:
            cnt *= 10

print(cnt)
