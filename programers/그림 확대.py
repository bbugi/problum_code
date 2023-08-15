# 코딩테스트 연습 > 코딩 기초 트레이닝 > 그림 확대

pic1 = [".xx...xx.", 
        "x..x.x..x", 
        "x...x...x", 
        ".x.....x.", 
        "..x...x..", 
        "...x.x...", 
        "....x...."]

pic2 = ["x.x", 
        ".x.", 
        "x.x"]

k = 3

answer = []

for i in range(len(pic2)) :
    resize = ''

    for j in range(len(pic2[0])) : 
        resize += pic2[i][j] * k

    for _ in range(k) : 
        answer.append(resize)
print(answer)