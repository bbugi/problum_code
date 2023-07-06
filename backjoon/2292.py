# 벌집 (브2)
# https://www.acmicpc.net/problem/2292

'''
구현, 수학
'''

n = int(input())
cnt = 1
beehouse = 1

while n > beehouse:
    beehouse += 6 * cnt
    cnt += 1

print(cnt)