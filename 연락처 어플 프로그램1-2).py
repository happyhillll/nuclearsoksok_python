print('메뉴를 선택하세요')
print('1:추가')
print('3:찾기')
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
    elif menu==3:
        find_name=input('이름으로 찾기: ')
        
        for i in datalist:
            if find_name==i[0]:   #i의 첫번째[0]=이름
                print(i[1],i[2])
                print('찾았습니다')
            elif find_name!=i[0]:
                print('해당정보가 없습니다')
        
    elif menu==0:
        break
    else:
        print('입력 오류')
               