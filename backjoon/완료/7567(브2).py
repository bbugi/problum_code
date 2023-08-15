# 그릇 (브2)
# https://www.acmicpc.net/problem/7567

'''
구현, 문자열
'''

s = input()
ans = 10
for i in range(len(s)-1):
    if s[i] == s[i+1] :
        ans += 5
    if s[i] != s[i+1] :
        ans += 10

print(ans)
