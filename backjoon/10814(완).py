# 나이순 정렬 (실5)
# https://www.acmicpc.net/problem/10814

'''
정렬할때 인자가 2개이상일때 인자 순서대로 정렬하려면
sorted(리스트, key = lambda x : (x[0], x[1]) )


[안정 정렬]
같은 수가 있을 때 입력된 순서대로 정렬을 한다면 안정 정렬

[불안정 정렬]
정렬 방식에 따라서 같은 수가 정렬된다.
나중에 입력된 수가 앞으로 정렬되는 경우가 생김


input 변수에 저장하는 방법
x, y = map(str, input().split())
리스트 변수 = input().split() 
x, y = input().split() # 입력받는 값이 변수와 동일해야 함

'''


# ====== 문제 풀이 ==========

import sys
input = sys.stdin.readline

n = int(input())

m_list = []
for _ in range(n):
    x, y = map(str, input().split())
    # x_list = input().split()
    # x, y = 
    
    m_list.append([int(x), y])

# print(m_list)
sorted_m = sorted(m_list, key = lambda x : x[0])
# sorted_m = sorted(m_list)

for i in sorted_m:
    print(*i)

# for i in range(n):
#     print(*sorted_m[i], end='\n') 
    # 이렇게 하면 프린트시 숫자가 str형이라서 틀렸다고 나오는듯
    # print(int(sorted_m[i][0]), end=' ') # 숫자로 바꿔도 
    # print(sorted_m[i][1])
    
    