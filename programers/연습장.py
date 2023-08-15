# # # # cipher = "dfjardstddetckdaccccdegk"
# # # # code = 4
# # # # ans = ''
# # # # for i in range(len(cipher)):
# # # #     if (i+1) % code == 0 :
# # # #         ans += (cipher[i])
# # # # print(ans)

# # # # from collections import deque
# # # # alpha = [chr(i) for i in range(97, 123)]
# # # # # print(alpha)

# # # # alpha = deque(alpha)
# # # # alpha.rotate(1)
# # # # print(list(alpha))

# # # # age = 23
# # # # for i in str(age):
# # # #     print(i)


# # # # mys = 'hello'
# # # # mys = list(mys)

# # # # num1 = 1
# # # # num2 = 2

# # # # print(mys)
# # # # myss = []

# # # # for i in range(len(mys)):
# # # #     if (i != num1) and (i != num2) :
# # # #         myss.append(mys[i])
# # # #     if i == num1 :
# # # #         myss.append(mys[num2])
# # # #     if i == num2 :
# # # #         myss.append(mys[num1])
    
# # # # print(myss)
# # # # answer = ''.join(myss)
# # # # print(answer)


# # # # order = 23436492123
# # # # order = list(map(int, str(order)))

# # # # for i in order:
# # # #     if i % 3 == 0:

# # # # s = "heLLo"

# # # # mystr = list(s.lower())
# # # # mystr.sort()
# # # # mystr = ''.join(mystr)
# # # # print(mystr)


# # # # s = "We are the world"
# # # # s = list(s)
# # # # answer = []
# # # # for i in s:
# # # #     if i in answer :
# # # #         pass
# # # #     else:
# # # #         answer.append(i)

# # # # answer = ''.join(answer)
# # # # print(answer)


# # # # num_list = [1, 2, 3, 4, 5, 6, 7, 8]
# # # # n = 2

# # # # answer = []

# # # # for i in range(len(num_list)//n):
# # # #     print(i)
# # # #     answer.append(num_list[n*i : n*(i+1)])
    
# # # # print(answer)
# # # # n = 7
# # # # ans = 1
# # # # answer = 0
# # # # for i in range(1, 11):
# # # #     # print(i)
# # # #     ans *= (i)
# # # #     # print(ans)
# # # #     if n >= ans:
# # # #         answer = i

# # # # print(answer)

# # # # array = [15, 11, 13]
# # # # n = 14
# # # # min = 100
# # # # answer = 0

# # # # array.sort()
# # # # for i in array :
# # # #     num = abs(i - n)
# # # #     if min > num:
# # # #         min = num
# # # #         answer = i
# # # # print(answer)

# # # # i = 1
# # # # j = 13
# # # # k = 1
# # # # cnt = 0
# # # # num_list = []
# # # # for n in range(i, j+1) :
# # # #     num_list.extend(map(int, list(str(n))))

# # # # print(num_list)
# # # # print(num_list.count(k))


# # # # emergency = [1, 2, 3, 4, 5, 6, 7]

# # # # e = emergency.copy()
# # # # e.sort(reverse=True)

# # # # print(emergency)
# # # # print(e)
# # # # ans = []
# # # # for i in emergency:
# # # #     if i in e :
# # # #         ans.append(e.index(i)+1)

# # # # print(ans)


# # # # my_string = "aAb1B2cC34oOp"

# # # # s = my_string.lower()
# # # # print(s)

# # # # alpha = [chr(i) for i in range(97, 123)]

# # # # for a in alpha:
# # # #     s = s.replace(a, ' ')
    
# # # # print(s)

# # # # num_list = list(map(int, s.split()))
# # # # print(num_list)



# # # # s = "hello"

# # # # s_list = list(s)
# # # # s_list.sort()

# # # # for i in s_list :
# # # #     if s_list.count(i) == 1:
# # # #         print(i)



# # # # s = "1 2 Z 3"

# # # # s_list = list(s.split())
# # # # num_list = []

# # # # for i in s_list:
# # # #     if i != 'Z':
# # # #         num_list.append(int(i))
# # # #     if i == 'Z' :
# # # #         num_list.pop()
# # # # print(num_list)

# # # from collections import deque

# # # A = 'apple'
# # # B = 'elppa'

# # # a = deque(A)
# # # b = deque(B)

# # # cnt = 0
# # # print(a)
# # # print(b)
# # # if a == b :
# # #     print(0)

# # # else:
# # #     for i in range(len(a)) :
# # #         if a != b :
# # #             a.rotate(1)
# # #             cnt += 1

# # #     if cnt == len(a) :
# # #         print(-1)

# # # print(cnt)


# # # import itertools
# # # spell = ["z", "d", "x"]

# # # dic = ["def", "dww", "dzx", "loveaw"]

# # # new = list(itertools.permutations(spell, len(spell)))

# # # for n in new:
# # #     if ''.join(n) in dic :
# # #         print(1)


# # # db = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]
# # # id_pw = ["rabbit04", "98761"]

# # # answer = 'fail'

# # # for i in range(len(db)) :
# # #     if db[i][0] == id_pw[0] and db[i][1] == id_pw[1] :
# # #         answer = 'login'
    
# # #     if db[i][0] == id_pw[0] :
# # #         if db[i][1] != id_pw[1] : 
# # #             answer = 'wrong pw'
    
# # # print(answer)

# # # from collections import deque

# # # anslist = []
# # # numlist = [1, 2, 3, 4, 5, 6]
# # # res = []
# # # n = 4

# # # for i in numlist :
# # #     anslist.append(i-n)

# # # print(anslist)

# # # for i in sorted(anslist, key=lambda x :[abs(x), -x]):
# # #     print(i)
# # #     print('1 : ', anslist.index(i))
# # #     print('2 : ', numlist[anslist.index(i)])
# # #     res.append(numlist[anslist.index(i)])

# # # print(res)


# # my_string = "He11oWor1d"
# # overwrite_string = 		"lloWorl"
# # s = 2


# # word = my_string[:s] + overwrite_string + my_string[len(overwrite_string) + s:]

# # print(word)



# # my_string = 'programmers'
# # alp = 'r'
# # ans = ''
# # for i in my_string:
# #     if i == alp:
# #         ans += alp.upper()
# #     ans += i
# # print(ans)




# # code = "abc1abc1abc"

# # def solution(code):
# #     answer = ''
# #     mode = 0
# #     for i in range(len(code)):
# #         if mode == 0 :
# #             if code[i] != '1' :
# #                 if i % 2 == 0 :
# #                     answer += code[i]
# #                     print(answer)
# #             elif code[i] == '1' :
# #                 mode = 1
                
# #         elif mode == 1 :
# #             if code[i] != '1' :
# #                 if i % 2 != 0 :
# #                     answer += code[i]
# #                     print(answer)
# #             elif code[i] == '1' :
# #                 mode = 0
        
# #     return answer if answer != '' else 'EMPTY'

# # print(solution(code))


# # a = 3
# # d = 4

# # included = [True, False, False, True, True]
# # numbers = list( a+(d*i) for i in range(len(included)))

# # print(numbers)


# # arr = [0, 1, 2, 3, 4]
# # q = [[0, 3],[1, 2],[1, 4]]

# # for i in q:
# #     tmp = arr[i[0]]
# #     arr[i[0]] = arr[i[1]]
# #     arr[i[1]] = tmp

# # print(arr)




# arr = [0, 1, 2, 4, 3]

# queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]


# answer = []
# for q in queries : 
#     s = q[0]
#     e = q[1]
#     k = q[2]
    
#     tmp = []
#     for i in arr[s:e+1] :

#         if i > k :
#             tmp.append(i)
    
#     print(min(tmp) if len(tmp) > 0 else -1)

# arr = [0, 1, 2, 4, 3]

# queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]
# answer = []
# for q in queries:
#     s = q[0]
#     e = q[1]
#     k = q[2]

#     for i in range(s, e+1):
#         if i % k == 0 :
#             arr[i] += 1
# print(arr)

# ans = []
# for i in range(10, 21) :
#     if i % 5 != 0:
#         pass

#     snum = str(i)
#     num_ox = True

#     for s in snum :
#         if s != '0' and s != '5' :
#             num_ox = False
    
#     if num_ox == True:
#         ans.append(i)

# if len(ans) == 0 :
#     ans.append(-1)
# print(ans)


# my_string = "rermgorpsam"
# queries = [[2, 3], [0, 7], [5, 9], [6, 10]]

# for q in queries:
#     s = q[0]
#     e = q[1]

#     # my_string = my_string[:s] + my_string[e:s:-1] + my_string[e:]

#     # print(my_string[:s])
#     # print()
#     # print(''.join(reversed(my_string[s:e+1])))
#     my_string = my_string[:s] + ''.join(reversed(my_string[s:e+1])) + my_string[e+1:]

#     print(my_string)



# numbers = [2, 5, 2, 6]
# cnt = {}

# for i in numbers:
#     if i in cnt.keys():
#         cnt[i] += 1
#     else:
#         cnt[i] = 1

# if len(set(numbers)) == 1:
#     print(1111* numbers.pop())

# elif len(set(numbers)) == 4:
#     print(min(numbers))

# elif len(set(numbers)) == 2:
#     if 3 in cnt.values():
#         p = [k for k, v in cnt.items() if v == 3][0]
#         q = [k for k, v in cnt.items() if v == 1][0]
#         print((10*p+q)**2)
#     else:
#         p, q = cnt.keys()
#         print((p+q) * abs(p-q))
# else:
#     p = [k for k, v in cnt.items() if v == 2][0]
#     q, r = [k for k in numbers if p != k]
#     print(q*r)


# quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
# answer = []
# for q in quiz:
#     l = list(map(str, q.split()))

#     num1 = int(l[0])
#     num2 = int(l[2])
#     num3 = int(l[4])

#     oper1 = l[1]

#     if oper1 == '+' :
#         ans = num1 + num2
#         if ans == num3 :
#             answer.append('O')
#         else :
#             answer.append('X')

#     elif oper1 == '-' :
#         ans = num1 - num2
#         if ans == num3 :
#             answer.append('O')
#         else:
#             answer.append('X')


# print(answer)




# sides = [11, 7]
# ans = 0

# for i in range(1, max(sides)+1) :
#     if max(sides) < i+min(sides) :
#         # print(i)
#         ans += 1

# for i in range(max(sides)+1, sum(sides)):
#     if i < sum(sides) :
#         # print(i)
#         ans += 1


# print(ans)




# keyinput =  ["right", "right", "right", "right", "right", "left"]
# board = [9,5]
# answer = [0,0]

# x = y = 0

# b_x = board[0] // 2
# b_y = board[1] // 2

# for key in keyinput :

#     if key == 'left' :
#         x -= 1
#     if key == 'right' :
#         x += 1
#     if key == 'up' :
#         y += 1
#     if key == 'down' :
#         y -= 1

#     if x > b_x :
#         x = b_x
#     if x < b_x * -1 :
#         x = b_x * -1
#     if y > b_y :
#         y = b_y
#     if y < b_y * -1 :
#         y = b_y * -1

# answer = [x,y]

# print(answer)




# polynomial = "1"
# x_cnt = 0
# n_cnt = 0

# lp = list(map(str, polynomial.split()))
# print(lp)

# for l in lp :
#     if 'x' in l :
#         if l == 'x' :
#             x_cnt += 1
#         else :
#             x_cnt += int(l.replace('x',''))

#     elif l != '+' :
#         n_cnt += int(l)

# if x_cnt == 0 :
#     print(f'{n_cnt}')
# elif n_cnt == 0:
#     if x_cnt == 1:
#         print('x')
#     else:
#         print(f'{x_cnt}x')
# else:
#     if x_cnt == 1:
#         print(f'x + {n_cnt}')

#     else:
#         print(f'{x_cnt}x + {n_cnt}')







# board = [[0, 0, 1], 
#          [0, 0, 0], 
#          [0, 0, 0]]

# n = len(board)

# xy = []


# num = 0
# for i in range(n) : # 행
#     for j in range(n): # 열
#         if board[i][j] == 1:
#             xy.append([i,j])
# # print(xy)
# for x, y in xy :
#     for a in range(-1, 2): # 행
#         for b in range(-1, 2): # 열
#             if 0 <= x+a < n and 0 <= y+b < n:
#                 board[x+a][y+b] = 1
# print(board)

# for i in range(n):
#     num += sum(board[i])

# print(num)


# a= {'일본','중국','한국'}
# a.add('중국')
# print(a)
# a.add('북한')
# print(a)
# a.remove('일본')
# print(a)
# a.update({'홍콩', '한국', '베트남'})
# print(type(a))
# print(a)

# #  중국 한국 북한 홍콩 베트남

# my_string="Programmers"

# answer = [0] * 52
# alp = [chr(i).upper() for i in range(97, 123)]
# alp.extend([chr(i) for i in range(97,123)])
    
# print(alp)

# for s in my_string :
#     for i in range(len(alp)) :
#         if s == alp[i]:
#             answer[i] += 1
# print(answer)


# answer = ''
# my_string = "apporoograpemmemprs"
# idx = [1, 16, 6, 15, 0, 10, 11, 3]

# str_idx = [i for i in range(len(my_string))]


# for i in idx:
#     for s in str_idx:
#         if i == s:
#             str_idx.remove(s)

# for s in str_idx:
#     answer += my_string[s]

# print(answer)






# arr = [1, 2, 1, 2, 1, 10, 2, 1]
# # arr = [1]
# idx2 = []
# answer = []
# for idx in range(len(arr)):
#     if arr[idx] == 2 :
#         idx2.append(idx)

# # print(idx2)

# if len(idx2) == 0 :
#     answer.append(-1)
#     print(answer)

# else:
#     answer.extend(arr[idx2[0] : idx2[-1]+1])
#     print(answer)


num_list = [12, 4, 15, 1, 14]
answer = 0

for num in num_list:
    while num >= 1:
        print(answer, num)
        if num % 2 == 0:
            num = num // 2
            answer += 1
        elif num % 2 != 0 :
            num = num-1
            # answer += 1
        


