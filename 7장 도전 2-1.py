import random
word =['반짝이는','별빛들','깜빡이는','불 켜진','건물','우린','빛나고','있네','각자의 방','각자의','별에서']
input('타자게임 시작 (엔터 입력) ')
w=random.choice(word)
n=1
correct=0
while True:
    print('문제',n,'(종료 0):',w)
    my=input()
    if my=='0':
        break
    elif my==w:
        print('맞음!!\n')
        w=random.choice(word)
        correct+=1
    else:
        print('틀림!다시!\n')
    n+=1


print('맞힌 문제 개수: ',str(correct)+',','정답률: ',str((correct/(n-1))*100)+'%')