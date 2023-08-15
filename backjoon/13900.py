# 순서쌍의 곱의 합 (실4)
# https://www.acmicpc.net/problem/13900

''' 풀이 6. sum(list)를 for문 바깥에서 미리 계산한 뒤 접근
시간복잡도 이해가 어려워 챗gpt한테 기존의 코드를 주고 시간복잡도를 구해달라고 했다.
for문 안에서 sum(list)를 반복해서 진행하여 O(N^2)의 시간복잡도가 발생

기존의 풀이 접근은
1 2 3 4 가 주어질 떄
1*(2+3+4) + 2*(3+4) + 3*(4)의 연산을 for문 안에서 진행

for문 안에서 sum 연산을 진행시키지 않고
(1+2+3+4) 를 먼저 더해둔 값을 변수에 저장해두고 진행
더한 값에서 기존에 주어진 수를 차례로 빼고, 곱셈을 진행하면 됨
'''
import sys
input = sys.stdin.readline

N = int(input()) # 입력받을 정수의 개수
num_list = list(map(int, input().split())) # N개의 정수를 부여받음
total_sum = sum(num_list) # num_list의 합을 미리 계산하여 저장

ans = 0
for num in num_list:
    total_sum -= num
    ans += num * total_sum

print(ans)











# import sys
# from collections import deque
# # import itertools


# input = sys.stdin.readline

# N = int(input()) # 입력받을 정수의 개수
# # num_list = list(map(int, input().split())) # N개의 정수를 부여받음

# num_list = deque(map(int, input().split()))
# # print(num_list)



''' 풀이 5 deque 활용해보기
deque의 pop은 O(1)의 속도이고, list의 pop은 O(n)의 실행속도 발생
list대신 deque를 활용하여 풀어보자
참조 : https://wellsw.tistory.com/122
'''
# ans = 0
# for i in range(len(num_list)-1):
#     popNum = num_list.popleft()
#     ans += popNum * sum(num_list)

# print(ans)



''' 풀이 4. pypy3으로 제출해도 75% 에서 시간초과 발생
풀이 3에서 사용한 방법에서 while 문이 아니라 for문으로 변경해보기
그리고 pop 대신 인덱스 사용해서 작업하기 - 인덱스 활용시 시간이 더 오래 걸림...
'''
# ans = 0
# for i in range(len(num_list)-1):
#     popNum = num_list[i]
#     ans += popNum * sum(num_list[i+1:])

# print(ans)



''' 풀이 3. 시간초과 발생
이중 포문 사용시 시간초과 발생, itertools 사용시 메모리 초과 발생..
풀이 2번과 동일한 접근인데 이중 포문을 사용하지 않고 구할 수 있는지?

왜 계속 시간초과가 발생하는 걸까!??!?!?

리스트.pop()의 경우 리스트의 크기가 커질수록 비례하여 실행시간도 늘어난다.
'''
# ans = 0
# while True :
#     if len(num_list) == 1:
#         break
#     else:
#         popNum = num_list.pop() # 리스트에서 pop 함수의 시간복잡도는 o(1)이다..
#         ans += popNum * sum(num_list)

# print(ans)




''' 풀이 2. 시간 초과 발생 (이중 포문이라서..?)
굳이 조합으로 만들 필요 없이 index를 통해서도 풀이가 가능해 보임
그런데 이게 과연 itertools의 combinations 함수를 사용하는 것보다
빠르고, 메모리 사용량이 적을지??
'''
# ans = 0
# for i in range(len(num_list)-1) :
#     for j in range(i+1, len(num_list)) :
#         ans += num_list[i] * num_list[j]
# print(ans)






''' 풀이 1. 메모리 초과 발생 
 두 수를 뽑는 모든 경우에 대해 각각의 곱을 구한 뒤 더해줘라
 itertools 라이브러리의 combinations 함수를 사용하면 조합을 구할 수 있음
'''
# set_num = tuple(itertools.combinations(num_list, 2))
# # print(set_num)

# ans = 0
# for i in range(len(set_num)) :
#     ans += set_num[i][0] * set_num[i][1]

# print(ans)


