# 소수 (브2)
# https://www.acmicpc.net/problem/2581

'''
수학, 정수론, 소수 판정

m 이상 n 이하의 자연수 중 
소수인 것을 모두 골라 소수의 합과 최솟값 찾기
'''
from collections import deque
import math

m = int(input())
n = int(input())

# numbers = [i for i in range(m, n+1)]
# dq = deque([i for i in range(2, 11)])
ans = deque([])


for i in range(m, n+1) :
    ans.append(i)
    # print(ans)
    for j in range(2, int(math.sqrt(i))+1) :
            if i % j == 0:
                ans.remove(i)
                break

if 1 in ans :
     ans.remove(1)

if len(ans) == 0 :
    print(-1)
else:
    print(sum(ans))
    print(ans[0])



