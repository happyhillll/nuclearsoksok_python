print('<< 369게임 >>')
num=int(input('1부터 어디까지 진행할까요? '))

for i in range (1,num+1):
    if i%10==3 or i%10==6 or i%10==9:
        print('짝',end=' ')
    else:
        print(i,end=' ')