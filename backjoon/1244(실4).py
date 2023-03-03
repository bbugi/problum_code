# 스위치 켜고 끄기 (실4)
# https://www.acmicpc.net/problem/1244

'''
구현, 시뮬레이션 문제
'''

# ===== 문제 풀이 =====


'''

# 반례
10
1 1 1 1 1 0 1 0 0 1
4
1 4
2 6
1 3
2 3

1 1 1 0 0 0 0 1 1 1

'''

def boy(switch_num, switch_length, switch_list):
    for i in range(1, switch_length+1):
        if i % switch_num == 0:
            if switch_list[i] == 0 :
                switch_list[i] = 1
            else:
                switch_list[i] = 0
                
                
def girl(switch_num, switch_length, switch_list):
    # for i in range(1, switch_length+1):
    # if switch_list[switch_num] == 0:
    #     switch_list[switch_num] == 1
    # else:
    #     switch_list[switch_num] == 0
    
    for j in range(0, switch_length):
        if 0 < (switch_num - j) and (switch_num + j) < n+1: 
            # print(j, switch_list[switch_num-j], switch_list[switch_num+j])
            if switch_list[switch_num-j] == switch_list[switch_num+j]:
                if switch_list[switch_num-j] == 0:
                    switch_list[switch_num-j] = 1
                    switch_list[switch_num+j] = 1
                else:
                    switch_list[switch_num-j] = 0
                    switch_list[switch_num+j] = 0
            else:
                break # 연속된 수를 확인했을 때 같은 숫자가 아니라면 비교를 멈춰야 하기때문에 break 걸어주기


                
n = int(input())

switch_list = ['']
# 켜진 스위치 : 1, 꺼진 스위치 0
switch_list.extend(list(map(int, input().split())))

# print(switch_list)


stu = int(input())

for i in range(stu):
    gender, s_num = map(int, input().split())
    # gender = 1 : 남학생, 2 : 여학생
    
    # 남학생이라면 자기가 받은 수의 배수인 스위치를 작동시킨다.
    if gender == 1:
        boy(s_num, n, switch_list)
        # print(switch_list)
    if gender == 2:
        girl(s_num, n, switch_list)
        # print(switch_list)
        

# 20개씩 끊어서 출력하는 법 블로그 참조
# https://jae04099.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-11721-%EC%97%B4-%EA%B0%9C%EC%94%A9-%EB%81%8A%EC%96%B4-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0
for i in range(1, len(switch_list)+1, 20):
    print(*switch_list[i:i+20])