def price(menu):
    if menu==1:
        print('아메리카노 2500원')
    elif menu==2:
        print('카페라떼 3000원')
    elif menu==3:
        print('바닐라라떼 3000원')
    else:
        print('메뉴가 없음')
    
menu=int(input('메뉴선택(1:아메리카노/1:카페라떼/3:바닐라라떼)'))
price(menu)