h=int(input('키 입력: '))
w=int(input('몸무게 입력: '))
bmi= w/((h/100)*(h/100))

if bmi < 18:
    result = '저체중'
elif 18 <= bmi < 23:
    result = '정상'
elif 23 <= bmi < 25:
    result = '과체중'
else:
    result = '비만'

print('bmi: %.2f, %s'% (bmi,result))