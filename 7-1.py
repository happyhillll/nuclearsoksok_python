students=[]
sum=0

num=int(input('학생 수 입력: '))
for i in range(num) :
    print('<<',i+1,'번째 학생 정보 입력 >>')
    name=input('학생 이름 입력 : ')
    score=int(input('%s 점수 입력: ' % name))
    students.append([name,score]) #학생 리스트에 저장
    sum+=score  #총점 구함

for info in students : #학생 정보 출력을 위한 for문
    print('이름: %s, 점수: %d' % (info[0],info[1]))
print('학생들 점수 평균: %5.2f' % (sum/num))
