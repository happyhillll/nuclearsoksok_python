vote={'가평':0,'대성리':0,'남이섬':0,'청평':0}
print(vote)

print('Best MT Spot')
while True:
    area=input('area:')
    if not area:break
    vote[area]=vote[area]+1

print(vote)
f=open('vote.txt','w')
for aarea,vvote in vote.items():
    f.write(f'{aarea}:{vvote}\n')  #f-string 이용!!!!!
f.close()  #하.. 이거 하는데 한시간 걸렸네 ....