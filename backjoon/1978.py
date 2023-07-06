# 소수 찾기 (브2)
# https://www.acmicpc.net/problem/1978

'''
수학, 정수론, 소수 판정
'''

'''
소수 : 1보다 큰 자연수 중 1과 자기 자신 외에는 나누어지지 않는 수
'''

# 소수 찾는 알고리즘 만들기
# 참조 블로그 : https://veggie-garden.tistory.com/17

def isPrime(n): # n이라는 숫자가 소수인지 확인해달라
    for i in range(2, n): # 2부터 n-1까지의 숫자로 n을 나눈다.
        if n % i == 0: # 만약 나누어 진다면 바로 False를 리턴
            return False 
    return True # n-1까지 나눠지지 않으면 





# 문제 풀이

import sys
input = sys.stdin.readline

n = int(input())

numbers = map(int, input().split())

# print(numbers)

sosu = 0

for num in numbers:
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
        if error == 0:
            sosu += 1

print(sosu)