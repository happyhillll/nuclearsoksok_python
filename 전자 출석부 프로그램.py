day=int(input('한 학기 수업주차 입력 : '))
att_book=[0]*day   #수업 주차 만큼 리스트를 0으로 초기화

for i in range(day):
    print('%d주차 강의에 출석하셨나요?'% (i+1))
    att_book[i]=int(input('출석은 1, 결석은 0 >>>'))

print(att_book)

cnt=att_book.count(0)
att=att_book.count(1)

print('결석 횟수 : %d' % cnt)
print('출석 횟수 : %d' % att)