# 로또 (실2)
# https://www.acmicpc.net/problem/6603

'''
수학, 조합론
백트래킹, 재귀
'''

import itertools

while True:
    k_list = list(map(int, input().split()))
    k = k_list[0]
    s = k_list[1:]
    
    s_comb = list(itertools.combinations(s, 6))
    for i in s_comb:
        print(*i)
    print()
    
    
    if k_list[0] == 0:
        break
     