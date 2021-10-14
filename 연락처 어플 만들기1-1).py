print('메뉴를 선택하세요')
print('1:추가')
print('0:종료')
datalist=list()
while True:
    
    menu=int(input('메뉴선택:'))
    if menu==1:
        name=input('이름:')
        tel=input('연락처:')
        email=input('email:')
        datalist.append((name,tel,email)) 
        print(datalist)
    elif menu==0:
        break
    else:
        print('입력 오류')
               