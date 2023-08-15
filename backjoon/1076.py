# 저항 (브2)
# https://www.acmicpc.net/problem/1076

'''
구현
'''

color = ["black", "brown","red","orange",
         "yellow","green","blue","violet",
         "grey","white"]

ans = ''

for i in range(3):
    s = input()
    if s in color:
        if i == 0:
            if s == 'black':
                pass
            else:
                ans += str(color.index(s))

        elif i == 1:
            ans += str(color.index(s))
        
        else:
            ans += '0' * color.index(s)
# print(ans)
# print(set(ans))
if set(ans) == 0 :
    print(0)
else:    
    print(ans)



# color = ["black", "brown","red","orange",
#          "yellow","green","blue","violet",
#         "grey","white"]

# ans = ""

# for i in range(3):
#     s = input()
#     for c in color:
#         if i == 0 :
#             if s == 'black' :
#                 pass
#             else:
#                 if s == c :
#                     ans += str(color.index(c))
#         elif i == 1:
#             if s == c:
#                 ans += str(color.index(c))
#         else:
#             if s == c:
#                 ans += "0" * color.index(c)
# if len(set(ans)) == 1:
#     print(0)
# else:
#     print(ans)