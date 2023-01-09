'''
# 스타트와 링크
구현으로 분류되어 있는 문제입니다
주어지는 입력을 이중배열로 잘 받은 후에 위의 완전 탐색을 사용하여 풀어보세요
잘 안되면 파이썬 라이브러리의 itertools를 검색해보세요

# 코드 참조 블로그
# https://bingbing-study.tistory.com/206
# 해당 블로그 보고 다시 공부하기
'''


import sys
import itertools
input = sys.stdin.readline

n = int(input())
lst=[]

for _ in range(n):
    lst.append(list(map(int, input().split())))
# print(lst)

# 팀1 vs 팀2 로 나눌려면
members = []
for i in range(n):
    members.append(i)
# print(members)

# 팀을 뽑아야 하는데 팀당 n//2명으로 묶여야 하므로 combinations에 n//2로 묶을거라고 선언
# 멤버가 4명일때 팀으로 묶일 수 있는 경우의 수는 한 팀당 6개이다

teams = []
for team in list(itertools.combinations(members, n//2)):
    teams.append(team) # i와 j를 하나로 묶은 것?
    # print(team)
# print(teams)

# a팀, b팀으로 나누어보자
A = []
B = []
for i in range(len(teams)//2): #팀을 2개로 나눠야 하므로 //2 해주기?? 근데 이러면 경우의 수가 안맞지않아?
    # print(teams[i])
    temp = list(itertools.combinations(teams[i], 2))
    # print(len(temp)) # 1?
    a_team = []
    for j in range(len(temp)):
        a_team.append( lst[temp[j][0]][temp[j][1]] + lst[temp[j][1]][temp[j][0]] )
        print('a_team:', a_team)
    A.append(sum(a_team))
    print('A:', A)

    temp2 = list(itertools.combinations(teams[-i-1], 2)) # 반대를 의미
    b_team = []
    for j in range(len(temp)):
        b_team.append( lst[temp2[j][0]][temp2[j][1]] + lst[temp2[j][1]][temp2[j][0]])
        print("b_team :", b_team)
    B.append(sum(b_team))
    print('B:', B)

mini = []
for i in range(len(A)):
    mini.append(abs(A[i] - B[i]))

print(min(mini))

