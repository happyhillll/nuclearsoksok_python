f=open('weather.txt')
for line in f:
    num,low,high=line.split(",")
    avg=(float(low)+float(high))/2
    print("%s월 평균기온은 %.2f입니다." % (num,avg))