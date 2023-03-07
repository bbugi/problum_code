# 보물 (실4)
# https://www.acmicpc.net/problem/1026

'''
수학
그리디 알고리즘
정렬
'''

# ===== 문제 풀이 =====


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

num_list = []
for i in range(n):
    num_list.append(a[i] * b[i])
print(sum(num_list))



    
