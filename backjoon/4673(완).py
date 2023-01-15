# 셀프 넘버 (실5)
# https://www.acmicpc.net/problem/4673
# 단계별로 풀어보기 - 함수

'''
브루트포스 알고리즘
분해합 문제와 동일한 알고리즘 사용
함수로 만들기
'''

# ==== 제출 답안 ====
num_list = [i for i in range(1,10001)]

for i in range(1, 10001):
    num = i + (i // 1000) + (i // 100)%10 + (i // 10)%10 + (i % 10)
    if num in num_list:
        num_list.remove(num)

for i in range(len(num_list)):
    print(num_list[i])


# 참조 풀이 ============
# https://sunning-10.tistory.com/m/entry/%EB%B0%B1%EC%A4%80-python-4673%EB%B2%88-%EC%85%80%ED%94%84-%EB%84%98%EB%B2%84%ED%95%A8%EC%88%98

# def d(n):
#     num = n + (n // 1000) + (n // 100)%10 + (n // 10)%10 + (n % 10)
#     return num

# num_list = [i for i in range(1,10001)]

# for n in range(1, 10001):
#     if d(n) in num_list:
#         num_list.remove(d(n))

# for i in range(len(num_list)):
#     print(num_list[i])





# ==== 문제 풀이 추론 과정 ====
# import sys

# num_list = [i for i in range(1,10001)]
# # print(num_list)

# num = 1
# while num <= 10000:
#     for i in range(1, 10000):
#     # print(i)
#         if num == i + (i // 1000) + (i // 100)%10 + (i // 10)%10 + (i % 10):
#             num += 1
#             continue
#         else:
#             num_list.append(i)
#             num += 1
# print(num_list)
# for num in range(1, 10000):
#     if num != i + (i // 1000) + (i // 100)%10 + (i // 10)%10 + (i % 10):
#         print(i)
#         i += 1
#     else:
#         i += 1
#         pass

# def d(n):
#     num = n + (n // 1000) + (n // 100)%10 + (n // 10)%10 + (n % 10)
#     return num












