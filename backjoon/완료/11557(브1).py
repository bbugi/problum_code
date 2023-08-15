# yangjojang of the year (브1)
# https://www.acmicpc.net/problem/11557

t = int(input())

for _ in range(t):
    n = int(input())
    top_l = 0
    top_s = False
    for _ in range(n):
        s, l = map(str, input().split())
        l = int(l)
        if l > top_l:
            top_s = s
            top_l = l
    print(top_s)
        
        