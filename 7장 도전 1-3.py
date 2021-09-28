import random
word = ['반짝이는','별빛들','깜빡이는','불 켜진','건물','우린','빛나고','있네','각자의 방','각자의','별에서']
input('타자게임 시작 (엔터 입력) ')
w=random.choice(word) #랜덤한 원소를 choice 
n=1  #몇번째 문제
while True:
    print('문제',n,'(종료0):',w)
    my=input()
    if my == '0':
        break
    elif my == w:
        print('맞음!!\n')
        w=random.choice(word)
    else:
        print('틀림!다시!\n')
    n += 1