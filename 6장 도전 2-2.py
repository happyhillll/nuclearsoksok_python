a=int(input("1차 점수 입력: "))
b=int(input("2차 점수 입력: "))
if 50<=a and 50<=b and a+b/2>=70:
    print("합격")
else: 
    print("불합격")