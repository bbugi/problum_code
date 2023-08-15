



# ===== 2741 (브5) N 찍기 ==================
# import sys
# for i in range(1, int(sys.stdin.readline())+1):
#     print(i)


# ===== 2743 (브5) 단어 길이 재기 ==================
# import sys

# n = sys.stdin.readline().lower()
# print(len(n)-1)




        
        


# ===== 11718 (브5) 그대로 출력하기 ==================

# while True:
#     try:
#         word = input()
#         print(word)
#     except:
#         break


# ===== 16394 (브5) 홍익대학교 ==================
# print(int(input()) - 1946)


# ===== 26082 (브5) WARBOY ==================

# a, b, c = map(int, input().split())
# print( 3 * c * b//a )


# ===== 13277 (브5) 큰 수 곱셈 ==================

# a, b = map(int, input().split())
# print(a * b)


# ===== 15727 (브5) 조별과제를 하려는데 조장이 사라졌다 ==================

# l = int(input())

# if l%5==0:
#     t = l // 5
# else:
#     t = l // 5 + 1 

# print(t)


# ===== 4101 (브5) 크냐? ==================

# while True:
#     a, b = map(int, input().split())
#     if a > 0 and b > 0:
#         if a > b:
#             print("Yes")
#         elif a <= b:
#             print("No")
#     elif a == 0 and b == 0:
#         break


# ===== 14581 (브5) 팬들에게 둘러싸인 홍준 ==================
# print(f''':fan::fan::fan:
# :fan::{input()}::fan:
# :fan::fan::fan:''')


# ===== 25372 (브5) 성택이의 은밀한 비밀번호 ==================
# n = int(input())

# for i in range(n):
#     pw = list(input())
#     if len(pw) >= 6 and len(pw) <= 9:
#         print("yes")
#     else:
#         print("no")



# ===== 25372 (브5) 와이버스 부릉부릉 ==================

# n, k = map(int, input().split())

# for _ in range(n):
#     a, b = map(int, input().split())
#     if a == 0:
#         print("비와이")



# ===== 17256 (브5) 달달함이 넘쳐흘러 ==================
 
# a = list(map(int, input().split()))
# c = list(map(int, input().split()))

# print(*[c[0]-a[2], c[1]//a[1], c[2]-a[0]])


# ===== 20492 (브5) 세금 ==================

# n = int(input())
# print(int(n*0.78), int((n*0.8)+(n*0.2)*0.78))


# ===== 1264 (브4) 모음의 개수 ==================
# an = ['a','e','i','o','u']
# while True:
#     count = 0
#     sens = list(input().lower())

#     if sens[0] == "#":
#         break
    
#     for sen in sens:
#         if sen in an:
#             count += 1
#     print(count)


# ===== 2440 (브4) 별 찍기-3 ==================

# for i in range(int(input()), 0, -1):
#     print("*"*i)


# ===== 2441 (브3) 별 찍기-4 ==================
# n = int(input())

# for i in range(1,n+1):
#     print(" "*(i-1), "*"*(n+1-i), sep="")


# ===== 2442 (브3) 별 찍기-5 ==================
# n = int(input())

# for i in range(1, n+1):
#     print(" "*((2*(n-i))//2) ,"*"*(2*i-1), sep='')



# ===== 1152 (브2) 단어의 개수 ==================
# sentences = input().split()
# print(len(sentences))

# ===== 2742 (브4) 기찍 N ==================
# n = int(input())

# for i in range(n, 0, -1):
#     print(i)


# ===== 15964 (브5) 이상한 기호 ==================

# a, b = map(int, input().split())
# print((a+b)*(a-b))


# ===== 15680 (브5) 연세대학교 ==================
n = int(input())
if n == 0 :
    print('YONSEI')
elif n == 1 :
    print('Leading the Way to the Future')