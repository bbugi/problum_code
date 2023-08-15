# 직사각형에서 탈출 (브3)
# https://www.acmicpc.net/problem/1085

'''
수학, 기하학
'''

x, y, w, h = map(int, input().split())
sub = []

sub.append(x)
sub.append(y)
sub.append(w-x)
sub.append(h-y)

print(min(sub))


