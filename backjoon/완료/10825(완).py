# 국영수 (실버4)
# https://www.acmicpc.net/problem/10825

'''
정렬 알고리즘 문제

대문자 소문자도 구분해야함..
아스키 코드...?

문자 정렬 참조 블로그
https://blockdmask.tistory.com/564

대소문자문자리스트.sort() 결과
대소문자 리스트.sort()는 대문자 ABCD 순으로 다 나온 후에,
소문자 abcd 순으로 정렬이 되는 것을 볼 수 있습니다. 
이는, 문자 자체를 아스키코드 값에 대응해서 숫자로 판단하기 때문인데요

'''


# ======== 문제 풀이 =========

import sys
input = sys.stdin.readline

n = int(input())
scores = []

for i in range(n):
    # 이름, 국어, 영어, 수학 순으로 입력
    scores.append(input().split())
    scores[i][1] = int(scores[i][1])
    scores[i][2] = int(scores[i][2])
    scores[i][3] = int(scores[i][3])
    
# 정렬 순서
# 국어 (내림차순), 영어(오름차순), 수학(내림차순), 이름(오름차순 - 대문자부터 출력(아스키코드에서 대문자가 작은 숫자임)
scores.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

# sorted의 경우 문자는 자동으로 정렬이 안됨.. (문자가 포함된 리스트의 경우 정렬하려면
# len(x)를 넣어줘야 한다.. 왜??)
# scores = sorted(scores, key = lambda x : (-x[1], x[2], -x[3], x[0], len(x)), reverse=False)

for i in range(n):
    print(scores[i][0])
