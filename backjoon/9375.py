# 패션왕 신해빈 (실3)
# https://www.acmicpc.net/problem/9375

'''
수학, 자료구조
조합론, 해시를 사용한 집합과 맵
'''

# 종류별로 옷을 입을 수 있는 모든 경우의 수에 모든 옷을 안 입는 경우를 빼주면 된다.
# 

t = int(input())

for _ in range(t):
    cloth = {}
    result = 1
    
    n = int(input())
    for _ in range(n):
        
        














# import itertools


# t = int(input())

# for _ in range(t):
#     n = int(input())
    
#     wear_list = []
#     w_dict = {}
    
#     for _ in range(n):
#         wear, type_w = map(str, input().split())
        
#         wear_list.append((wear, type_w))
        
#         print(wear_list)
    
#     for w, t in wear_list:
#         if t in w_dict:
#             w_dict[t].append(w)
#         else:
#             w_dict[t] = [w]
                
#     for key in w_dict.keys():          
#         l = w_dict.get(key)
        
#         print(l)