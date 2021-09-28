print('<<369게임 시작>>')
num=int(input('1부터 어디까지 진행할까요? '))

for i in range (1,num+1):
    if i%10==3 or i%10==6 or i%10==9:
        print('짝',end=' ')
    elif i%10==0:
        print('따봉',end=' ')
    else:
        print(i,end=' ')