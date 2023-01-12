# 수 정렬하기 3 (브1)
# https://www.acmicpc.net/problem/10989

# 정렬 문제
# 오름차순 정렬 결과 출력
# 주어지는 수는 10,000보다 작거나 같은 자연수

# ===== 문제 풀이 2 - 계수 정렬 코드 사용 - 메모리 초과 발생 =====
import sys

n = int(sys.stdin.readline())
count = [0] * (10000+1)

array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

# print(array)

for i in range (len(array)):
    count[array[i]] += 1

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

