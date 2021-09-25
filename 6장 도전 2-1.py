a=int(input("첫 번째 수 입력: "))
b=int(input("두 번째 수 입력: "))
c=input("원하는 연산 기호 하나 입력: ")

if c == '+':
    result = a+b
elif c == '-':
    result = a-b
elif c == '*':
    result = a*b
elif c == '/':
    result = a/b
       
print(a,c,b,"=",int(result))