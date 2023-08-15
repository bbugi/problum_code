# 달팽이는 올라가고 싶다 (브1)
# https://www.acmicpc.net/problem/2869

'''
수학문제
'''

################


a, b, v = map(int, input().split())

if v < a :
    print(1)

else:
    if (v-a) % (a-b) == 0:
        print((v-a) // (a-b) + 1)
    else:
        print((v-a) // (a-b) + 2)

