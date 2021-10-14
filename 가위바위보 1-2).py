import random

com_count=0
human_count=0
a=['가위','바위','보']
while True:
    if com_count or human_count ==3: break
    human=input('가위,바위,보 중 하나를 입력하시오: ')
    com=a[random.randint(0,2)]  # 0부터 2까지의 수 중에 하나의 정수 선택
    print('컴퓨터: %s'%com)
    if human=='가위':
        if com=='바위':
            print('컴퓨터 승')
            com_count+=1
        elif com=='보':
            print('당신 승')
            human_count+=1
        else:
            print('비겼습니다.')
    elif human=='바위':
        if com=='가위':
            print('당신 승')
            human_count+=1
        elif com=='보':
            print('컴퓨터 승')
            com_count+=1
        else:
            print('비겼습니다')
    elif human=='보':
        if com=='가위':
            print('컴퓨터 승')
            com_count+=1
        elif com=='바위' :
            print('당신 승')
            human_count+=1
        else:
            print('비겼습니다') 
    else:
        print('입력 오류')   
    
if int(com_count)>int(human_count):
    print('컴퓨터 승!')
elif int(human_count)>int(com_count):
    print('당신 승!')