# 참외밭 (실2)
# https://www.acmicpc.net/problem/2477


# ========= 문제 풍리 ============

# 첫번째 줄에 참외의 개수 
# 동 : 1, 서 : 2, 남 : 3, 북 : 4
# min, max 로 풀이 가능 - 아니었다!!
# 빼야하는 숫자는 순서로 정해야 한다!

# 빼야하는 상자의 크기 규칙은 같은 방향으로 반복되는 구간이 있는데 그곳의 중간지점이다!
# 아래의 경우 3,1,3,1이 반복되고 그 안에서 가운데에 위치한 1 60 / 3 20이 빼야하는 상자의 크기가 된다

# 4 50
# 2 160
# --
# 3 30
# 1 60
# 3 20
# 1 100
# --


import sys
input = sys.stdin.readline

n = int(input())

'''
딕셔너리는 인덱싱이 불가능하고 key값으로만 해야하기 때문에
key list와 value list를 만들어서 처리하자
반복은 확인했는데 중복값을 어떻게 확인해야 할 지 모르겠다
그리고 시작은 육각형의 임의의 위치에서 시작한다

'''


key_list = []
value_list = []

for _ in range(6):
    a, b = map(int, input().split())
    key_list.append(a)
    value_list.append(b)

if key_list[3] == 2:
    small_v, small_h = value_list[2:4]

elif key_list[3] == 1:
    small_v, small_h = value_list[3:5]
   

if key_list == 1  or key_list == 2:
    




# ==========딕셔너리로 풀다가 잘못된 접근(min, max) 으로 인해 실패한 코드 ==========
# dct = {}
# for _ in range(6):
#     a, b = map(int, input().split())
#     dct[f'{a}'] = b
    
    # if 'a' not in dct.keys():
        # dct[f'{a}'] = b
        
        # 왜 else문으로는 빠지지 않는것인가.
        # else문으로 빠지지 않아서 작은 수로 교체가 불가능하다

    # else:
    #     print("else문 진입")
    #     if b < dct[f'{a}'].value():
    #         print("b:", b)
    #         print(dct[f'{a}'].value())
    #         dct[f'{a}'] = b
# print(dct)


# # 1,2 / 3,4 로 묶어서 아예 하나로 볼까??
# lst_h = [1,2]
# lst_v = [3,4]

# for i in lst_h:
#     print(dct.values(i))

