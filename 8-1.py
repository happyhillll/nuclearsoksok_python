score=[]
p,f=0,0
cnt=int(input('수강 과목 수 : '))

for i in range(cnt):
    s=int(input('score %d : ' % (i+1)))
    score.append(s)

for i in range(cnt):
    if score[i]>=80:
        p+=1
    else:
        f+=1

print('pass: ',p)
print('fail: ',f)