# 치킨 TOP N (실4)
# https://www.acmicpc.net/problem/11582

'''
정렬
분할 정복

분할 정복? - 병합 정렬에서 사용함
1. 분할 : 동일한 타입의 하위 문제로 큰 문제를 분할 (ex. 정렬의 경우 숫자가 1개가 남을때까지 분할)
2. 정복 : 재귀적으로 하위문제 해결
3. 병합 : 적절히 해결된 문제를 사용해 큰 문제 해결

'''

# 병합 정렬 알고리즘
# https://m.blog.naver.com/sunbi5252/221977857377 참조

# 문제에서 k는 병합 단계를 말 하는 것인데,
# 쉽게 얘기하면 

# 리스트 m이 주어질 때
from heapq import merge


def merge_sort(m):
    if len(m) <= 1: # 사이즈가 0이거나 1인 경우, 바로 리턴
        return m

    mid = len(m) // 2
    print(mid)
    left = m[:mid]
    print(left)
    right = m[mid:]
    print(right)
    
    # 리스트의 길이가 1이 될때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


m = list(input().split())

merge_sort(m)


# 병합 정렬 merge 사용해서 풀면 오히려 시간초과가 나올 가능성이 높다.
# 그래서 분할 정복 / 병합 정렬 문제가 나오면
# 걍 4/4개로 나눈 다음에 바로 sort 해서 푸는게 나을 수도 있다.

# 퀵 정렬 4일때는 정렬 
# 