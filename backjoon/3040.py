# 백설 공주와 일곱 난쟁이 (브2)
# https://www.acmicpc.net/problem/3040

'''
브루트포스 알고리즘(완전탐색)

9개의 숫자 중에서 7개를 뽑아 합이 100이 되면 된다
즉, 9개의 숫자를 다 합친 상태에서 2개의 숫자를 빼면 100이 된다.
'''

# arr = []
# for i in range(9) :
#     arr.append(int(input()))

# num1 = 0
# num2 = 0

# for i in range(8) : # 0~8 인덱스까지 존재
#     for j in range(i+1, 9) : # 0~8 인덱스까지 존재
#         # print(i,j, '답:::',sum(arr)-arr[i]-arr[j])
#         if sum(arr) - (arr[i] + arr[j]) == 100:
#             num1 = arr[i]
#             num2 = arr[j]
#             # print(num1, num2)
#             break

# arr.remove(num1)
# arr.remove(num2)

# print(*arr, sep='\n')


n = int(input())
answer = [[0 for i in range(n)] for i in range(n) ]

print(answer)

