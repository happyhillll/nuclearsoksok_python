f=open('score1.txt')
print('이름,합계,평균')
for line in f:
    name,mid,final=line.split()
    
    hap=int(mid)+int(final)
    avg=int(hap)/2
    print(name,hap,avg)
f.close()