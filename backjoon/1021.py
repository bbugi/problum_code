# 회전하는 큐 (실3)
# https://www.acmicpc.net/problem/1021

'''
자료구조, 덱
'''

from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))

queue = deque([i+1 for i in range(n)])

cnt = 0

while True:
    for i in range(n):
        if nums[i] == queue[i] :
            queue.popleft()
            nums.remove(nums[i])
        
        elif nums[i]
    

