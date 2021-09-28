score=[]
total=0
for i in range(5):
    s=int(input('score: '))
    score.append(s)

for i in score:
    total += i

avg = total/5

print('total: ',total)
print('avg: ',avg)