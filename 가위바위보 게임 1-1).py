import random

a=['가위','바위','보']
human=input('가위,바위,보 중 하나를 입력하시오: ')
com=a[random.randint(0,2)]  # 0부터 2까지의 수 중에 하나의 정수 선택
print('컴퓨터: %s'%com)
if human=='가위':
    if com=='바위':
        print('컴퓨터 승')
    elif com=='보':
        print('당신 승')
    else:
        print('비겼습니다.')
elif human=='바위':
    if com=='가위':
        print('당신 승')
    elif com=='보':
        print('컴퓨터 승')
    else:
        print('비겼습니다')
elif human=='보':
    if com=='가위':
        print('컴퓨터 승')
    elif com=='바위' :
        print('당신 승')
    else:
        print('비겼습니다') 
else:
    print('입력 오류')       