# 주어진 수가 작을 경우 앞에 0을 붙여 두자리 수로 만들고
# 각 자리 숫자를 더한다
# 주어진 수의 가장 오른쪽 자리의 수와
# 합의 가장 오른쪽 자리의 수를 이어 붙이면 새로운 수를 만들수 있다.

# 무조건 2자리 수가 나오므로 오른쪽 자리의 수는 숫자[1]로 인덱스 활용?

# ex
# 26
# 2 + 6 = 8
# 새로운 수 : 68
# 6 + 8 = 14
# 새로운 수 : 84
# 8 + 4 = 12
# 새로운 수 : 42
# 4 + 2 = 6
# 새로운 수 : 26 (4번만에 원래 수로 돌아온다. 사이클은 4이다)

# n = list(map(int,input().zfill(2)))
# print(n)

# m = list(map(int,str(sum(n)).zfill(2)))
# print(m)

# k = int(str(n[1]) + str(m[1]))

# print(k)




n = list(map(int,input().zfill(2)))
answer = n
n1 = 0
root=1
while True:
    if answer == n1:
        break
    elif n1 == 0:
        m = list(map(int,str(sum(n)).zfill(2)))
        root += 1
        k = int(str(n[1]) + str(m[1]))
        n1 = k
        continue
    else:
        m = list(map(int,str(sum(n1)).zfill(2)))
        root += 1
        k = int(str(n[1]) + str(m[1]))
        n1 = k
        continue


    