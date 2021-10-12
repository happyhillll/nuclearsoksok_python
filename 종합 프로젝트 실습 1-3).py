def sell_menu():
    print('**자판기 판매 메뉴**')
    for i in range(5):
        print('{} : {} {}'.format(i+1,menu[i],price[i]))    

def drink(price):
    global money
    while True:
        num=int(input('메뉴 선택(종료:0): '))
        if num == 0:
            break
        if money<price[num-1]:
            print('잔액 부족')
        else:
            print(menu[num-1],'구입 완료')
            money=money-price[num-1]
            print('잔액: ',money)
            print()

def change():
    global money
    c500= money//500
    money= money-(c500*500)
    c100= money//100
    money= money-(c100*100)
    print('자판기 종료')
    print('coin500 : %d개 반환' % c500)
    print('coin100 : %d개 반환' % c100)
    print('나머지 : %d 반환' % money)
    
menu=['콜라','사이다','환타','커피','생수']
price=[500,500,600,600,400]

sell_menu()

money=int(input('돈을 투입하세요 : '))
print()

drink(price)
change()