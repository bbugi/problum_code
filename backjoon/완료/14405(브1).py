# 피카츄 (브1)
# https://www.acmicpc.net/problem/14405

'''
문자열
'''

import sys
input = sys.stdin.readline

sound = ['pi','ka','chu']
sentence = input().rstrip()

# print(sentence)

for s in sound :
    if s in sentence:
        sentence = sentence.replace(s,'.')
        # print(sentence)
        # print(set(sentence))

if '.' in set(sentence):
    if len(set(sentence)) == 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
