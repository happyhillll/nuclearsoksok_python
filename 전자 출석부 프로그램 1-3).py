def save(day,att):
    for i in range(day):
        print('%d주차 강의에 출석하셨나요?'% (i+1))
        att_book[i]=int(input('출석은 1, 결석은 0 >>>'))

def count():
    cnt=att_book.count(0)
    att=att_book.count(1)

def ratio_print():
    ratio= int(att)/int(day)    
    att_ratio= ratio*100
    absent_ratio= 100-int(att_ratio)

day=int(input('한 학기 수업주차 입력 : '))
att_book=[0]*day
cnt,att=0,0
ratio,absent_ratio,att_ratio=0,0,0

save(day,att_book)
count()
ratio_print()

if ratio >= 0.3:
    print('수업일수 부족입니다.')

print('결석 횟수 : %d' % cnt)
print('출석 횟수 : %d' % att)
print('결석률은 %.f%%입니다.' % absent_ratio)  # %% : percentage 같이 표시하고 싶을때 
print('출석률은 %.f%%입니다.' % att_ratio)