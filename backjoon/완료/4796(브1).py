# 캠핑 (브1)
# https://www.acmicpc.net/problem/4796

i = 0

while True:
    ans = 0
    i += 1
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break
    else:
        # print('v//p',v//p)
        # print('l',l)
        # print('(v//p) * l', (v//p) * l)
        # print('v%p',v%p)

        if v % p > l :
            ans = (v // p) * l + l
        else:
            ans = (v // p) * l + (v%p)

        print(f'Case {i}:', ans)
    # ans = (v // p) * l + (v%p)
    # print(f'Case {i}:', ans)