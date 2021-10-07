fin=open('data2.txt.rtf')
fout=open('output4.txt','w')
lines=fin.readlines()

hap=0

for line in lines:
    line=line.rstrip() #개행문자 제거
    score=int(line) 
    hap += score

avg=hap/len(lines)

ahap="hap:%d\n"%hap
aavg="avg:%d\n"%avg

fout.write(str(ahap))
fout.write(str(aavg))

fin.close()
fout.close()
