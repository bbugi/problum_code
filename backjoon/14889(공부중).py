# 스타트와 링크 (실2)
# https://www.acmicpc.net/problem/14889

'''
구현으로 분류되어 있는 문제입니다
주어지는 입력을 이중배열로 잘 받은 후에 위의 완전 탐색을 사용하여 풀어보세요
잘 안되면 파이썬 라이브러리의 itertools를 검색해보세요

# 코드 참조 블로그
# https://bingbing-study.tistory.com/206
# 해당 블로그 보고 다시 공부하기
'''

# ========= 혼자 문제풀이 =============

# import sys
# from itertools import combinations

# input = sys.stdin.readline

# n = int(input())
# table = []
# for _ in range(n):
#     table.append(list(map(int, input().split())))

# print(table)

# # 멤버 조합하기 (전체 인원 리스트)
# n_lst = [ i for i in range(n)]
# print(n_lst)

# # 한 팀당 모일 수 있는 팀원의 모든 조합 구하기
# members = list(combinations(n_lst, n//2))
# print(members)

# # members_reverse = list(combinations(n_lst, n//2))
# # members_reverse.reverse()
# # print(members_reverse)
# a_teams = []
# print(len(members)//2) # 모든 조합에서 n/2개만 확인하면 된당
# for i in range(len(members)//2):
#     a_teams.append(members[i])
# print(a_teams) # a_teams에 들어갈 수 있는 팀원의 종류

# # 팀원의 조함에서 점수 확인하기
# for a_team in a_teams:
#     member_scores = list(combinations(a_team, 2))
#     print(member_scores)
    
# a_scores = []
# b_scores = []
# for i in range(len(member_scores)):
#     for j in range(len(member_scores)):
#         a = table[member_scores[j][0]][member_scores[j][1]] + table[member_scores[j][1]][member_scores[j][0]]
#         print(f"aaaaaaa{j}:", a)
#         print('table[member_scores[j][0]]', table[member_scores[j][0]])
#         print('table[member_scores[j][1]]', table[member_scores[j][1]])
        
#         a_scores.append(a)
#     print(a_scores)
# # print(a)
# # print(b)
    
    
    
    
    
    

# 팀원의 조합 안에서 점수 세기
# for member in members1:
#     print(member) # 팀원 누가 들어오는지
#     # print(len(member)) # 한팀에 있는 팀원 수  # 3
#     # 팀원간 능력치
#     mem_score = list(combinations(member, 2))
    
    
    
    
# member_score = list(combinations( , 2))






# ================================================
# # 축구를 위해 모인 사람 N (짝수)
# # N/2로 이루어진 스타트팀, 링크팀

# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n = int(input())

# # for i in range(n):
# #     for j in range(n):
# #         print(i,j)

# table = []
# for _ in range(n):
#     a = list(map(int, input().split()))
#     table.append(a) # 이중배열 만들기

# # print(table)

# # 팀을 나눠야 하는데 n/2명이 팀원이 된다.
# # 팀이 될수 있는 경우의 수 확인
# '''
# 01
# 02
# 03
# 12
# 13
# 23
# 이렇게 1팀으로 구성할수 있음
# 반대의 경우는 어차피 같은거라서 저 경우만 봐주면 된다
# '''


# ''' 내가 생각한 member출력하는 코드
# member = []
# for i in range(n-1, 0, -1):
#     for j in range(i):
#         member.append(tuple(map(int, (j,i))))
# print(member)
# 이 코드는 a, b팀에 넣는 순서에 규칙성이 없어서  사용할 수 없을 듯
# '''


# # ---
# # 각 멤버는 2명씩 나눠진다
# # 조합을 해보자 (itertools.combinations 사용해보자)

# members = []
# for i in range(n):
#     members.append(i)
# # print(members) # 멤버 수 풀어서 리스트에 담기


# member = combinations(members, n//2)
# teams = list(member)
# # print(teams)
#  # 2개씩 묶어서 조합 만들고 리스트에 담기

# # ---


# # 팀을 a, b로 나누기
# # a팀에 들어가면 b팀은 a팀의 반대로..?
# a_team = []
# b_team = []
# for team in teams:
#     print('team============:',team)
    
# print('teamssssss============:',teams)

# A = []
# B = []

# for i in range(len(teams)//2):
#     # print(len(teams)//2) # 10개만 보면 됨 (나머지 10개는 반대상황)
#     # print(teams[1])
#     temp = list(combinations(teams[i],2))
#     # print(temp)
#     for j in range(len(temp)):
#         # print(table[temp[j][0]][temp[j][1]] + table[temp[j][1]][temp[j][0]])
#         a_team.append(table[temp[j][0]][temp[j][1]] + table[temp[j][1]][temp[j][0]])
#         A.append(sum(a_team))

# for i in range(len(teams)//2):
#     # print(len(teams)//2) # 10개만 보면 됨 (나머지 10개는 반대상황)
#     # print(teams[1])
#     temp2 = list(combinations(teams[-i-1],2))
#     # print(temp)
#     for j in range(len(temp)):
#         # print(table[temp[j][0]][temp[j][1]] + table[temp[j][1]][temp[j][0]])
#         b_team.append(table[temp2[j][0]][temp2[j][1]] + table[temp2[j][1]][temp2[j][0]])
#         B.append(sum(b_team))

# mini = []
# for i in range(len(A)):
#     mini.append(abs(A[i] - B[i]))

# print(min(mini))



# mini = []
# for i in range(len(A)):
#     mini.append(abs(A[i] - B[i]))





        # print('team[0]============:',team)
        # print(']============:',len(team))

    
#         a_team.append(list(table[i_idx][j_idx]+ table[j_idx][i_idx])
#         b_team.append(table[n-1-i_idx][n-1-j_idx]+ table[n-1-j_idx][n-1-i_idx])

# # a팀과 b팀의 능력치 확인 가능
# print("a_team: ", a_team)
# print("b_team: ", b_team)

# # 능력치 차이 최소값 찾기
# minus_num = []
# for i in range(len(a_team)):
#     # print(i)
#     minus_num.append(abs(a_team[i] - b_team[i]))
#     # print('-------', minus_num)
#     # min_num = min(list(abs(a_team[i] - b_team[i])))
#     # print(min_num)
#     # print(min(minus_num))

# print(min(minus_num))
# # if abs(a_team[i] - b_team[i]) == min(minus_num):
# #     print(i)



# ====================================





# # 팀이 되는 경우를 a팀으로 생각하여 팀에 넣기
# a_team = []
# for i in range(len(teams)//2):
#     print(i)



# for i in range(len(teams)//2): #팀을 2개로 나눠야 하므로 //2 해주기?? 근데 이러면 경우의 수가 안맞지않아?
#     print(teams[i])
#     temp = list(itertools.combinations(teams[i], 2))
#     print(len(temp)) # 1?
#     a_team = []
#     for j in range(len(temp)):
#         a_team.append( lst[temp[j][0]][temp[j][1]] + lst[temp[j][1]][temp[j][0]] )
#         print('a_team:', a_team)
#     A.append(sum(a_team))
#     print('A:', A)

#     temp2 = list(itertools.combinations(teams[-i-1], 2)) # 반대를 의미
#     b_team = []
#     for j in range(len(temp)):
#         b_team.append( lst[temp2[j][0]][temp2[j][1]] + lst[temp2[j][1]][temp2[j][0]])
#         print("b_team :", b_team)
#     B.append(sum(b_team))
#     print('B:', B)

# mini = []
# for i in range(len(A)):
#     mini.append(abs(A[i] - B[i]))

# print(min(mini))













#  =============== 블로그 참조 문제 풀이 =============

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

# # 팀을 뽑아야 하는데 팀당 n//2명으로 묶여야 하므로 combinations에 n//2로 묶을거라고 선언
# # 멤버가 4명일때 팀으로 묶일 수 있는 경우의 수는 한 팀당 6개이다

teams = []
for team in list(itertools.combinations(members, n//2)):
    teams.append(team) # i와 j를 하나로 묶은 것?
    print('team==============:', team)
print('teams==============:',teams)

# a팀, b팀으로 나누어보자
A = []
B = []
for i in range(len(teams)//2): #팀을 2개로 나눠야 하므로 //2 해주기?? 근데 이러면 경우의 수가 안맞지않아?
    print(len(teams)//2)
    print(teams[i])
    temp = list(itertools.combinations(teams[i], 2))
    print(len(temp)) # 1?
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



# ===== 현우 풀이 =====

from collections import deque
import copy
import sys
import itertools

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ls = []
for i in range(n) :
    ls.append(i)
choice=list(itertools.combinations(ls,int(n/2)))

minval = 100

for i in range(int(len(choice)/2)) :
    tmp = list(itertools.permutations(choice[i],2))
    ver = list(itertools.permutations(choice[-i-1],2))
    tmpval, verval = 0, 0
    for j in range(len(tmp)) :
        tmpval += arr[tmp[j][0]][tmp[j][1]]
        verval += arr[ver[j][0]][ver[j][1]]
    if minval > abs(tmpval-verval) :
        minval = abs(tmpval-verval)   

print(minval)