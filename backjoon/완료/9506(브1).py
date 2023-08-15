# 약수들의 합 (브1)
# https://www.acmicpc.net/problem/9506

'''
수학, 구현, 정수론
'''

while True:
    n = int(input())
    ans = []
    s = ''

    if n == -1 :
        break

    else:
        for i in range(1, n) :
            if n % i == 0 :
                ans.append(i)

        if sum(ans) == n :
            print(n, '=', end=' ')
            for i in range(len(ans)) :
                if i < len(ans)-1 :
                    print(ans[i], '+', end=' ')
                else:
                    print(ans[i])

        else :
            print(n, 'is NOT perfect.')

