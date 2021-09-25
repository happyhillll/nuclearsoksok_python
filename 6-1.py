year=int(input('연도 입력: '))
if year % 4 == 0 and year % 100!=0 or year % 400==0 :
    print('%d 년은 윤년' % year)
else:
    print('%d 년은 윤년아님' % year)