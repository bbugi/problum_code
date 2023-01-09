'''
# 시험감독
간단하게 수학 수식계산으로 풀이 생각하고 코드 작성하면 돼요
처음에 틀릴 수 있는데 수식을 유연하게 고쳐보면서 output 보세요

# 문제 해석
시험장 n
i번 시험장에는 Ai명 존재

시험장 i번마다 존재?
감독관(총감독관, 부감독관)
총감독관 only 1명, 감시인원 B
부감독관 여러명 가능, 감시인원 C

'''

# import sys
# input = sys.stdin.readline

# # 시험장의 개수
# n = int(input())
# test_p = list(map(int, input().split()))
# B, C = map(int, input().split())
# # print(n, test_p, B, C)

# # 시험장 총괄
# # 총감독관의 수 = n / 감시인원 = n * B
# # 부감독관의 수 = n*x / 감시인원 = n * x * C
# # 필요한 감독관의 수 = n*(1+x)


# ovs = n
# for i in range(n):
#     if (test_p[i]-B) > 0:
#         # print('test',(test_p[i]-B))
#         # print(round((test_p[i]-B) / C , 0))
#         if round((test_p[i]-B) / C , 0) == 0:
#             # print(round((test_p[i]-B) / C , 0))
#             ovs += 1
#         else:
#             x = (test_p[i]-B) / C + 0.1
#         # print(round(x,0))
#             ovs += round(x,0)
#     else:
#         pass
            
# print(int(ovs))



# ================= 틀렸다고 나와서 다시 풀어보기 ===============

# import sys
# input = sys.stdin.readline

# n = int(input())
# test_p = list(map(int, input().split()))
# B, C = map(int, input().split())

# num = n

# for i in range(n):
#     if (test_p[i]-B) > 0: # 인원 중 총감독관이 볼 수 있는 인원 제외하고도 0이상일때
#         if ((test_p[i]-B) % C) != 0:
#             # print('===',((test_p[i]-B) % C))
#             num += (((test_p[i]-B) // C) + 1)
#         else:
#             num += 1
#     else:
#         pass
# print(num)

# ============== 또틀림!! 어디가 틀린거지?? =============

# 드디어 맞췄다!
import sys
input = sys.stdin.readline

n = int(input())
test_p = list(map(int, input().split()))
B, C = map(int, input().split())

num = n

for i in range(n):
    if (test_p[i]-B) > 0: # 인원 중 총감독관이 볼 수 있는 인원 제외하고도 0이상일때
        num += (test_p[i]-B) // C
        if (test_p[i]-B) % C != 0:
            num += 1
    else:
        pass
print(num)