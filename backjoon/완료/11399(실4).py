# ATM (실4)
# https://www.acmicpc.net/problem/11399

'''
그리디 알고리즘, 정렬
'''

n = int(input())

numbers = list(map(int, input().split()))

sorted_nums = sorted(numbers)
# print(numbers)
# print(sorted_nums)
ans = 0

for i in range(n):
    ans += sum(sorted_nums[:i+1])
print(ans)