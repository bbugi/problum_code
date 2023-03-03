# 색종이 만들기 (실2)
# https://www.acmicpc.net/problem/2630

'''
분할 정복, 재귀

https://moz1e.tistory.com/85 여기 블로그의 해답풀이 보면서 공부함
-> 분할정복 부분에 식에대한 이해가 잘 가지않음..

분할정복의 제대로 된 개념을 이해하지 못하면 문제 못품...
https://velog.io/@minidoo/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-2630%EB%B2%88-%EC%83%89%EC%A2%85%EC%9D%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0
다른 블로그의 해답 풀이 참조

function F(x):
    if F(x)가 간단 then:
        return F(x)를 계산한 값
        
    else:
        x를 x1, x2로 분할
        F(x1)과 F(x2)를 호출
        return F(x1), F(x2)로 F(x)를 구한 값

'''



# ===== 문제 풀이 =====

# 전체 종이의 한 변의 길이 n
n = int(input())

# 전체 종이를 2차원 배열로 생성하기
paper = [[] * n for i in range(n)] 
# 배열에 숫자를 바로 입력함 


# print(paper)

for i in range(n):
    a = list(map(int, input().split()))
    paper[i] = a  # 리스트 원소값으로 그냥 넣으려면 append가 아니라 그냥 = 으로 값을 부여해버리면 됨
    
# print(paper) # 값이 맞게 들어갔는지 확인

# 분할 정복의 개념을 사용하여 흰 색종이(0값만 존재), 파란 색종이(1값만 존재)
# 가 몇개가 있는지 확인하기

# 흰종이 개수 세기 
w_cnt = 0
# 파란종이 개수 세기
b_cnt = 0


# 분할정복 함수 생성 (색종이를 2등분씩 분할하기)
# x, y는 색종이의 좌표 시작점
def split_paper(x, y, n):
    global w_cnt, b_cnt
    color = paper[x][y]
    
    # 색종이 크기를 만들어주는 i, j
    for i in range(x, x+n):
        for j in range(y, y+n):
            
            # 나눈 색종이의 가장 앞의 값과 동일하지 않으면 색종이로 만들수 없으므로
            # 다시 분할해야한다.
            # 색종이를 분할할때는 정사각형 모양으로 분할해야 하므로 항상 4등분이 이루어진다,
            # 그래서 동일하지 않으면 4분할 범위로 재정의한 함수를 또 돌려야 하므로 
            # 재귀함수는 4개로 돌리게 된다.
            
            # 쿼드트리 ( 4갈래로 가지치기한 재귀함수 )
            if color != paper[i][j]:
                split_paper(x, y, n//2)
                split_paper(x, y+n//2, n//2)
                split_paper(x+n//2, y, n//2)
                split_paper(x+n//2, y+n//2, n//2)
                return
            
            
            # 병합정렬 => 분할정복
            
    
    # 함수 돌려서 나눠진 범위내에서 color값이 모두 동일한 애들만 이 조건문으로 접근하게 되는데
    # 여기서 color 가 0이라면 흰종이
    # color가 1이라면 파란종이로 분류되어 개수를 세면 된다.
    if color == 0:
        w_cnt += 1
    else:
        b_cnt += 1
        

split_paper(0,0,n)
print(w_cnt)
print(b_cnt)
                

    
    


