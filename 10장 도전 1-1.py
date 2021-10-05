fin=open('data2.txt.rtf')
fout=open('output.txt','w')
lines=fin.readlines()

hap=0

for line in lines:
    line=line.rstrip()
    score=int(line)
    hap += score

avg=hap/len(lines)
    
fin.close()
fout.close()