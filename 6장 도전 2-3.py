a=int(input("점수 입력: "))
if a >= 90:
    print("%d점은 A학점" %a)
elif 80<=a<=89:
    print("%d점은 B학점" %a)
elif 70<=a<=79:
    print("%d점은 C학점" %a)
elif 60<=a<=69:
    print("%d점은 D학점" %a)
else:
    print("%d점은 F학점" %a)