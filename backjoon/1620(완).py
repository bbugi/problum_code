# 나는야 포켓몬 마스터 이다솜 (실4)
# https://www.acmicpc.net/problem/1620

# 자료구조 - 해시를 사용한 집합과 맵 (해시 = 딕셔너리)

'''
# items() - 사전 데이터(키와 값을 쌍)을 리턴 (dict_items)
# for 반복문을 활용해 사전 데이터를 쉽게 출력할 수 있다.

딕셔너리의 key : value값 스왑하기
{value:key for key, value in num_dict.items()}
'''

# ==== 네번째 문제 풀이 - 통과 ======
# 딕셔너리 2개만들기

import sys
input = sys.stdin.readline

n, m= map(int, input().split())

# 포켓몬 도감 만들기
num_dict = {}
for i in range(n):
    num_dict[i+1] = input().rstrip()
name_dict = {value:key for key, value in num_dict.items()}
# 기존에 받은 num_dict의 키값과 밸류값을 반대로하여 새로운 딕셔너리로 생성

# print(num_dict) key(숫자) : value(문자) 형태의 딕셔너리
# print(name_dict) key(문자) : value(숫자) 형태의 딕셔너리

# 도감에서 값 찾기
for i in range(m): # key값으로 value값 찾기 -> 딕셔너리명.get(key값)
    find = input().rstrip()
    try: # 숫자 받았을 때
        print(num_dict.get(int(find)))
    except: # 문자 받았을 때
        print(name_dict.get(find))
 


# ==== 세번째 문제 풀이 - 시간초과 ======
# 해시(딕셔너리) 형태 사용하기
# value로 key 찾기에서 리스트 추가 생성됨
# import sys
# input = sys.stdin.readline

# n, m= map(int, input().split())

# poke_dict = {}
# # name_dict = {}

# for i in range(n):
#     poke_dict[i+1] = input().rstrip()

# print(poke_dict)

# for i in range(m):
#     find = input().rstrip()
#     try: # 숫자 받았을 때
#         print(poke_dict.get(int(find)))
#     except: # 문자 받았을 때 - value값으로 key 값 찾기
#         print(*[key for key, value in poke_dict.items() if value == find])
 


# ==== 두번째 문제 풀이 - 시간초과 ======
# 걍 리스트로 생각하고 인덱스 따로
# import sys
# input = sys.stdin.readline

# n, m= map(int, input().split())

# poke_list = []
# for i in range(n):
#     poke_list.append(input().rstrip())

# for i in range(m):
#     find = input().rstrip()
#     try:
#         print(poke_list.index(find)+1)
#     except:
#         print(poke_list[int(find)-1])





# ===== 첫번째 문제 풀이 - 시간초과 =======
# 인덱스를 같이 넣어서 작업

# import sys
# input = sys.stdin.readline

# n, m= map(int, input().split())

# poke_list = []
# for i in range(n):
#     poke_list.append((i,input().rstrip())) # rstrip()해줘서 개행문자 제거
#     # print(poke_list[i][0])

# for i in range(m):
#     find = input().rstrip()
#     for j in range(n):
#         try:
#             if int(find)-1 == (poke_list[j][0]):
#                 print(poke_list[j][1])
#         except:
#             if find == poke_list[j][1]:
#                 print(int(poke_list[j][0])+1)

