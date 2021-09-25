day31=[1,3,5,7,8,10,12]
day30=[4,6,9,11]
year=int(input('연도 입력: '))
month=int(input('월 입력: '))
if month <1 or month > 12 :
    print('존재하지 않는 월!!')
elif month in day31 :
    result=31
elif month in day30 :
    result=30
elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    result = 29
else :
    result = 28
print('%d년 %d월은 %d까지' % (year,month,result))