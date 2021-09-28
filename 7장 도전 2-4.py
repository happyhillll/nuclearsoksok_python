import random
print("<<컴퓨터가 생각한 1~20 숫자 맞추기>>")
com=random.randint(1,20)
cnt=0
while True:
    cnt+=1
    player=(int(input('숫자 입력(종료 0): ')))
    if player==0:
        break
    elif player == com:
        print('정답!')
        break
    elif player > com:
        print('더 작은 숫자 입력!')
    elif player < com :
        print('더 큰 숫자 입력!')
    if cnt==5:
        print('5번 시도 완료!')
        break