# 손익분기점 (브2)
# https://www.acmicpc.net/problem/1712

'''
수학 - 사칙연산 문제
while문으로 x를 하나씩 증가시키면서 풀면
시간이 너무 많이 걸린다(예시에 21억짜리도 있기때문에)
+=1씩 늘려서는 풀 수 없다고 봐야함
'''

# ===== 문제 풀이 ==================

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# 손익분기점이 되는 판매량 x
# b가 c보다 크거나 같으면 몇개를 팔아도 손익분기점이 존재할 수 없다(비용이 항상 수익보다 크기 때문에)

if b >= c :
    print(-1)
else:
    # cx - bx - a > 0 이 되어야 손익분기점이 넘는것
    # (c-b)x > a
    # x > a /(c-b) : x가 항상 a/(c-b)보다 커야하므로 +1을 해주자
    print(a//(c-b) + 1)