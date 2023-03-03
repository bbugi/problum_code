# 팰린드롬수 (브1)
# https://www.acmicpc.net/problem/1259

'''
구현, 문자열

팰린드롬 : 어떤 단어를 뒤에서부터 읽어도 똑같은 단어
'''


while True :
    n = int(input())
    # print(n)
    
    if n == 0 :
        break
    
    n_list = list(str(n))
    # print(n_list)
    
    # n_list를 그대로 reverse 해버리면 비교할 수가 없으므로, 
    # n_list를 reverse할 리스트로 복사 (m_list)
    # 리버스한 리스트와 원본 리스트를 비교해서 같으면 팰린드롬 수라고 볼 수 있다
    m_list = n_list.copy()
    m_list.reverse()
    # print(m_list)
    
    if n_list == m_list :
        print('yes')
    else:
        print('no')
    

    
    