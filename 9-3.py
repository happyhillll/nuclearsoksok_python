def max1(num1,num2):
    if num1>num2:
        print(num1)
    elif num1<num2:
        print(num2)
    else:
        print('두 수가 같습니다')
a=int(input('첫 번째 수 입력:'))
b=int(input('두 번째 수 입력:'))
max1(a,b)