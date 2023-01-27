# 계단오르기(실3)
# https://www.acmicpc.net/problem/2579

'''
다이나믹 프로그래밍으로 분류되어 있는 문젠데 처음에 많이 어려울거에요
다이나믹 프로그래밍이 뭔지부터 구글링해서 보세요
요약하면 다이나믹 프로그래밍은 리스트에서 서로 다른 index 간 관계성을 파악해서
문제 풀이하는 건데 이번 문제에서는 계단과 계단 사이의 어떤 관계가 있고 그 관계를
수식으로 어떻게 나타낼건지 생각해보면 돼요
'''

#  ========== 문제 풀이 =============




# ==== 현우 풀이 =====

# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        score = list()
        for i in range(n) :
            score.append(int(input()))
        return n, score

    n, score = getdata()
    dp = list(0 for _ in range(n))
    if n == 1:
        print(score[0])
    elif n == 2:
        print(score[0]+score[1])
    else :
        dp[0] = score[0]
        dp[1] = score[0]+score[1]
        dp[2] = max(score[0],score[1])+score[2]
        for i in range(3,n) :
            dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i])
        print(dp[n-1])