f=open('score2.txt')
print('이름,평균,학점')
for line in f:
    name,score=line.split()
    for i in line:
        if int(score)>=90:
            grade="A"
        elif int(score)>=80:
            grade="B"
        elif int(score)>=70:
            grade="C"
        elif int(score)>=60:
            grade="D"
        elif int(score)<60:
            grade="F"
    print(name,score,grade)

#인덴트 조심하기!!!!!!


