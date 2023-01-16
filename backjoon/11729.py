# 하노이 탑 이동 순서 (실1)
# https://www.acmicpc.net/problem/11729

# 알고리즘의 벽

# 재귀함수 - 기저조건이 필요함 (탈출조건)
# 등비수열
# 시작, 경유, 끝지점 print 만 하면 되는 문제였음

# ============ 문제 풀이 ===========

# ==== 지섭오빠 코드보고 공부하기 ====
def hanoi(n, start, dest, via): # (갯수, 시작, 도착, 경유)
    if n == 1:
        print(start, dest)
    else:
        hanoi(n-1, start, via, dest)    # ①n-1개의 원판을 [시작]에서 [경유]로 [도착]을 거처 이동
        print(start, dest)              # ②가장큰 n원판을 [시작]에서 [도착]으로 이동 출력
        hanoi(n-1, via, dest, start)    # ③옮겨둔 n-1개의 원판을 [경우]에서 [도착]으로 [시작]을 거처 이동
                                        # ①,③ n-1이동 2번 + n번째 이동 1번 -> a_n = 2a_(n-1) + 1 = 2(a_(n-1) + 1) - 1
                                        # (a_n + 1) = 2(a_(n-1) + 1) -> 첫항이 2, 공비가 2인 등비수열
                                        # a_n + 1 = 2^n
                                        # a_n = 2^n - 1
n = int(input())
print(2**n - 1)
hanoi(n, 1, 3, 2)
