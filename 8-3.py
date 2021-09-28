print('정수를 입력. 0 입력시 종료됨')
total=0
s=int(input('num: '))

while s!=0:
    total += s
    s=int(input('num: '))
    
print('총 합계 : ',total)