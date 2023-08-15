# 슈퍼 마리오 (브1)
# https://www.acmicpc.net/problem/2851

'''
구현, 브루트포스 알고리즘, 누적 합
'''
num_list = []
ans = 0
ans_list = []

for i in range(10):
    num_list.append(int(input()))
    ans += num_list[i]
    num_list[i] = ans
    ans_list.append(abs(ans-100))
# print(ans_list)

if min(ans_list) == 0 :
    print(num_list[ans_list.index(0)])
else:
    if ans_list.count(min(ans_list)) > 1:
        print(num_list[ans_list.index(min(ans_list)) + 1])
    else:
        print(num_list[ans_list.index(min(ans_list))])



