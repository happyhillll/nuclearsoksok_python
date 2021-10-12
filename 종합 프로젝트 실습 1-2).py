menu=['콜라','사이다','환타','커피','생수']   # 메뉴와 가격을 리스트에 초괴화
price=[500,500,600,600,400]   

print('**자판기 판매 메뉴**')   
for i in range(5): 
    print('{}:{}{}'.format(i+1,menu[i],price[i]))   # 자판기에 저장된 메뉴와 가격을 해당번호와 함께 출력한다.

print()

money=int(input("돈을 투입하세요: "))    # 자판기에 투입할 돈을 사용자로부터 입력받는다.
print()

while True:                        # 잔액이 부족할때까지 메뉴를 선택할 수 있도록 반복 구조를 사용한다. 
    num=int(input('메뉴 선택(종료:0): '))   #메뉴 선택번호와 프로그램 종료 번호를 입력받는다.
    if num==0:
        break
    if money<price[num-1]:   #price는 리스트니까 메뉴선택에서 누르는 int에서 1을 뺴줘야함. 
        print('잔액부족')
    else:                   #돈이 남을 경우, 음료를 화면에 반환하고, '구입완료' 메시지를 출력하고 잔액을 계산한다. 
        print(menu[num-1],'구입완료')
        money=money-price[num-1]
        print('잔액: ',money)
        print()
    
c500= money//500
money= money-(c500*500)
c100= money//100
money= money-(c100*100)
print('자판기 종료')
print('coin500 : %d개 반환' % c500)
print('coin100 : %d개 반환' % c100)
print('나머지 : %d 반환' % money)   # 자판기가 종료되고 최종 잔액을 출력한다. 