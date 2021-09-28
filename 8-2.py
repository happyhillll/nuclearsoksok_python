s=int(input('start num: '))
e=int(input('end num: '))

total=0

for i in range(e+1):
    if i % 3 != 0:
        total += i

print('3의 배수를 제외한 숫자의 합',total)