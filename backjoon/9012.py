# 괄호(실4)
# https://www.acmicpc.net/problem/9012

'''
자료구조, 문자열, 스택(리스트 사용) 문제
'''

from collections import deque

queue = deque()



# 테스트 케이스 t
t = int(input())

for i in range(t):
    queue.append(deque(input()))
# print(queue)
    
for q in queue:
    # print(q)
    # print(len(q))
    print(q[0])
        
    # if len(q) > 2:
        # print(q[0])

        
    
    
    
    
# print(q)

# for i in q:
#     while len(set(i)) == 2:
#         print(i)
#         # print(len(set(i)))
#         # print(len(i))
#         # q가 비어있지 않을 때 계속해서 돌리기
#         if i[0] == '(' and i[1] == ')':
#             i.popleft()
#             print('1번째',i)
#             i.popleft()
#             print('2번째', i)
#         else:
#             i.rotate(-2) # 음수로 해야지 앞에 있는게 뒤로 옮겨간다
#             # 양수 1로 하면 가장 오른쪽에 있는 값이 가장 앞으로 온다
            
#         if len(i) == 0:
#             print('YES')
#             break    
#         if i[0] == ')' and i[i] == '(':
#             print("NO")
#             break
#     else:
#         print("NO")
    
        
        

        