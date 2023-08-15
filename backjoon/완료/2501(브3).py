# 약수 구하기 (브3)
# https://www.acmicpc.net/problem/2501

'''
수학, 브루트포스 알고리즘
'''

n, k = map(int, input().split())
ans = []

for i in range(1, n+1) :
    if n % i == 0 :
        ans.append(i)

try:
    print(ans[k-1])
except:
    print(0)