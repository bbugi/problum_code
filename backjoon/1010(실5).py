# 다리 놓기 (실5)
# https://www.acmicpc.net/problem/1010

'''
수학, 조합론
다이나믹 프로그래밍
'''
# # 다이나믹 프로그래밍 : 모든 경우의 수를 연결하는 것..
# # 그런데 다리는 서로 겹쳐질 수 없다고 한다.
# # 그리고 서쪽의 n개의 사이트가 무조건 동쪽의 m개의 사이트보다 작거나 같다.
# # n개랑 m 개일때 조합 확인...


# import math

# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     print(n, m)    
#     cnt = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
#     print(cnt)




# ======= 팩토리얼 함수 만들어서 풀이하기

def s_factorial(n):
    num = 1
    for i in range(1, n+1):
        # print(i)
        num *= i
    return num

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    cnt = s_factorial(m) // (s_factorial(m-n) *(s_factorial(n)) )
    print(cnt)
