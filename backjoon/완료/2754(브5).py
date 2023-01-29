# ===== 2754 (브5) 학점계산 ==================
'''
sys로 받을때 개행문자 빠졌는지 확인 잘 할것
if문에 왜 안들어오나 했는데 개행문자까지 포함되서 못찾은것
'''

import sys
input = sys.stdin.readline

score_num = [4.3, 4.0, 3.7, 
             3.3, 3.0, 2.7, 
             2.3, 2.0, 1.7, 
             1.3, 1.0, 0.7,
             0.0]

score = ['A+', 'A0', 'A-', 
         'B+', 'B0', 'B-',  
         'C+', 'C0', 'C-',  
         'D+', 'D0', 'D-', 
         'F']

s_input = input().rstrip()

for idx in range(len(score)):
    if s_input == score[idx]:
        print(score_num[idx])