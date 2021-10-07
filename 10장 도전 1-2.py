f=open('data3.txt','a')
for i in range(3):
    w=input('word:')
    if not w:break
    f.write(w+'')
f.close()
f=open('data3.txt')
cnt=0
for line in f:
    line=line.rstrip()
    word=line.split()
    for w in word:
        cnt += 1
        print(w,end='')
print()
print('total word :',cnt)
f.close()    