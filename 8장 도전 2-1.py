phonebook={}
while True:
    a=input('1) 친구 등록 2) 검색 3) 종료 : ')
    if a == 3:
        break
    elif a == 1:
        name=input('name: ')
        phone=input('phone: ')
        phonebook[name]=phone 
    elif a == 2: 
        name=input('name: ')
        phone=phonebook[name]
        print(phone)      