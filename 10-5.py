vote={'가평':0,'대성리':0,'남이섬':0,'청평':0}
print(vote)

print('Best MT Spot')
while True:
    area=input('area: ')
    if not area: break
    vote[area]=vote[area]+1 #키 값 증가
    
print(vote)