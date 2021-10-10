f=open('score2.txt')
for line in f:
    name,score=line.split()

for i in line:
    if score>=90:
        grade=A
    elif score>=80:
        grade=B
    elif score>=70:
        grade=C
    elif score>=60:
        grade=D
    elif score<60:
        grade=F

print('이름,평균,학점')

while True:
    for k in f:
        print(name,score,grade)

