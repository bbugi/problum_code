# 설탕 배달 (실4)
# https://www.acmicpc.net/problem/2839

# 그리디 알고리즘

'''
3킬로, 5킬로로 나눠지면 최소 봉지수 출력
안나눠지면 -1 출력
분해합처럼 풀면 되는건가?
'''

# ========== 문제 풀이 ===========

# 제출 코드
# 코드 하나씩 뜯어서 해결은 했는데
# 어떤 알고리즘으로 풀리는 것인지 모르겠음
# 나중에 코드 다시 수정해볼 것

# 그리디 알고리즘을 생각해서 다시 풀어봐야함==============


n = int(input())
def bag(n):
    ans = []
    for x in range(0, n//5+1):
        for y in range(0, n//3+1):
            if n - 5*x - 3*y == 0:
                ans.append(x+y)

    if len(ans) == 0:
        return -1
    else:
        return min(ans)

print(bag(n))




# ==== 풀이 찾아가던 과정 =======
# n = int(input())
# print(n)

# n = 18
# x = 3
# y = 1

# if n - 5*x - 3*y == 0:
#     print('true')

# def bag(n):
#     answer = []
#     for x in range(0, n):
#         if n - 5*x == 0:
#             answer.append(x)
#         if n - 5*x !=
#             n = n - 5*x
#             for y in range(0, n):
#                 if n - 3*y == 0:
#                     answer.append(y)
                    
                
# #         for y in range(0, n//3+1):
# #             if n - 5*x - 3*y == 0:
# #                 print(x+y)
# #                 answer.append(x+y)
# #                 print('answer:' , answer)
# #                 return min(answer)

# n = int(input())
# print(bag(n))