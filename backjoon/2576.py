# 홀수 (브3)
# https://www.acmicpc.net/problem/2576

odd = []
for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        odd.append(num)

if len(odd) == 0 :
    print(-1)
else:
    print(sum(odd), min(odd), sep='\n')
