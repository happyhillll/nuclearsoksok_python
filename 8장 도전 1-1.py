import random

print('덧셈 게임')
score=0

while True:
    s=input('시작:아무키나,종료:0')
    if s=='0': break
    n1=random.randint(10,99)
    n2=random.randint(10,99)
    print(' {}+{}= '.format(n1,n2))
    ans=int(input('answer:'))
    if ans==n1+n2:
        print('정답')
        score += 10
    else:
        print('오답')
        score -= 5
print('score: ',score)