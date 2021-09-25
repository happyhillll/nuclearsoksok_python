month=int(input('월 입력: '))
if month < 1 or month >12 :
    print('존재하지 않는 월!!')
elif 3<=month<=5 :
    print(month,"월은 봄")
elif 6<=month<=8 :
    print(month,"월은 여름")
elif 9<=month<=11 :
    print(month,"월은 가을")
else:
    print(month,'월은 겨울')