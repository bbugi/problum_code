# 수 정렬하기 3 (브1)
# https://www.acmicpc.net/problem/10989

# 정렬 문제
# 오름차순 정렬 결과 출력
# 주어지는 수는 10,000보다 작거나 같은 자연수

# ===== 문제 풀이 2 - 계수 정렬 사용 - 맞춤 =====
import sys

n = int(sys.stdin.readline())
count = [0] * (10000+1)

# 리스트에 담는 만큼 메모리를 잡아먹는다.
# 굳이 리스트에 값을 담을 필요는 없다

# array = []
# for _ in range(n):
#     array.append(int(sys.stdin.readline()))

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1
# print(array)

for i in range(len(count)):
    for j in range(count[i]):
        print(i)

# ==== 문제 풀이1 - 메모리 초과 발생 ====

# import sys
# input = sys.stdin.readline

# n = int(input())

# num_list = []
# for _ in range(n):
#     num = int(input())
#     num_list.append(num)

# num_list.sort()
# print(*num_list, sep='\n')

