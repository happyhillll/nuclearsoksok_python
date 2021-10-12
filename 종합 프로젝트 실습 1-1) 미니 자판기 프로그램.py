menu=['콜라','사이다','환타','커피','생수']
price=[500,500,600,600,400]

print('**자판기 판매 메뉴**')
for i in range(5):
    print('{}:{}{}'.format(i+1,menu[i],price[i]))

print()

money=int(input("돈을 투입하세요: "))
print()

while True:
    num=int(input('메뉴 선택(종료:0): '))
    if num==0:
        break
    if money<price[num-1]:   #price는 리스트니까 메뉴선택에서 누르는 int에서 1을 뺴줘야함.
        print('잔액부족')
    else:
        print(menu[num-1],'구입완료')
        money=money-price[num-1]
        print('잔액: ',money)
        print()
    print('자판기 종료, 잔액 {} 반환'.format(money))    
        