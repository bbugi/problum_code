# 차량 번호판 1 (브1)
# https://www.acmicpc.net/problem/16968

'''
수학, 조합론
'''


# lst = list(input())

# cnt = 0
# if lst[0] == 'c':
#     cnt = 26
# else:
#     cnt = 10
    
# for i in range(1, len(lst)):
#     if lst[i] == 'c':
#         if lst[i] == lst[i-1]:
#             cnt *= 25
#         else:
#             cnt *= 26
#     else:
#         if lst[i] == lst[i-1]:
#             cnt *= 9
#         else:
#             cnt *= 10

# print(cnt)




# =================

form = {'c': 26, 'd': 10}
cd = input()

result = 1

for i in range(len(cd)):
  num = form[cd[i]]
  print(cd[i], form[cd[i]])
  if cd[i] == cd[i-1] and i> 0:
    num -= 1
  result *= num
  
print(result)