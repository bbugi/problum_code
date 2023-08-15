# 진법 변환 (브1)
# https://www.acmicpc.net/problem/11005

'''
수학, 구현

# n진수에 대한 개념 이해하기

10진수의 수를 n진수로 변환하려면
10진수를 n으로 나눠서 나오는 나머지 값을 가장 
나중에 연산된 나머지부터 출력하게 하면 됨.

'''

def n2ten (num, n) :
    result = []

    while num > 0 :
        m = num % n # 나머지 -> n진법의 값이 나옴
        num = num // n 
        # result.append(m)
        result.insert(0, m) # result 리스트에 0인덱스 위치에 m을 추가하는 함수
    return result

ans = [i for i in range(10)]

alp = [chr(s).upper() for s in range(97,123)]
# print(alp)

ans.extend(alp)
# print(ans[35])

num, n = map(int, input().split())
result = n2ten(num, n)

for i in result :
    print(ans[i], end='')