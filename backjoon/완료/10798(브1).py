# 세로읽기 (브1)
# https://www.acmicpc.net/problem/10798

'''
2차원 배열
구현, 문자열
'''

field = []
max_len = 0
new_word = []

for i in range(5):
    word = list(input())
    field.append(word)
    if len(word) > max_len:
        max_len = len(word)


for j in range(max_len):
    for i in range(5):
        try:
            new_word.append(field[i][j])
        except:
            pass

print(*new_word, sep='')