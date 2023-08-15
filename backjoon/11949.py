# 번호표 교환 (브2)
# https://www.acmicpc.net/problem/11949

'''
구현, 시뮬레이션
'''

# 학생 수 n
# 카드 개수 m (1 ~ m까지 존재)
# k번 카드는 k-1번 카드 쓴 다음 사용
# 1번 학생한테는 무조건 i번 카드를 부여??
# j번 학생은 j+1번 학생한테 카드를 넘김
# aj % i 의 값이 aj+1 % i 값보다 크면 카드 교환
# 마지막 학생은 카드를 받으면 버린다.
# m번 카드를 버리면 종료

n, m = map(int, input().split())
card = [0]
for i in range(n):
    card.append(int(input()))

# print(card)
# [3, 2, 8, 3, 1, 5] 학생이 가지는 번호표의 값
for i in range(1,m+1) :
    for j in range(1,n):
        # print('card[j]',card[j], card[j] % i)
        # print('card[j+1]::',card[j+1], card[j+1] % i )
        # print()
        
        if card[j] % i > card[j+1] % i :
            tmp = card[j]
            card[j] = card[j+1]
            card[j+1] = tmp

        # print(card)

print(*card[1:], sep='\n')