a = int(input())
b = int(input())

def math_ab(a, b):
    return (a+b, a-b, a*b)

print(*math_ab(a,b), sep='\n')
