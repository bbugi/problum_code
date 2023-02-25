# 패션왕 신해빈 (실3)
# https://www.acmicpc.net/problem/9375

'''
수학, 자료구조
조합론, 해시를 사용한 집합과 맵
'''

# 종류별로 옷을 입을 수 있는 모든 경우의 수에 모든 옷을 안 입는 경우를 빼주면 된다.
# 옷의 이름은 필요 없다.
# 옷 종류별로 조합만 가능하면 되기 때문에 옷 종류에 count 해서 숫자 생성


# ===== 문제 풀이 =====

t = int(input())
for _ in range(t):

# 딕셔너리에 키 값에 해당하는 값이 있으면 1씩 추가하는 코드
    counts = {}
    n = int(input())
    for _ in range(n):
        name, w_type = map(str, input().split())
        # print(name, w_type)
        if w_type not in counts:
            counts[w_type] = 1
        else:
            counts[w_type] += 1

    c_list = list(counts.values())
    # print(c_list)
    for i in range(len(c_list)):
        c_list[i] = c_list[i]+1
    
    ans = 1
    for i in c_list:
        ans *= i
    print(ans - 1)
        
    
    
        

        
        












# =========== 다른 접근으로 가능한지 풀어보기 ==========

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