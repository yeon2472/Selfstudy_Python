
A,B = map(int,input().split())

if (A>B) :
    print('>')
elif (A<B) :
    print('<')
else :
    print('==')


score = int(input())

if (score >= 90) :
    print("A")
elif (score >= 80) :
    print("B")
elif (score >= 70) :
    print("C")
elif (score >= 60) :
    print("D")
else :
    print("F")


## 윤년 알아내기
year = int(input())
if (year % 4 == 0) & (year % 100 != 0) | ( year % 400 == 0) :
    print(1)
else :
    print(0)

## 사분면
x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print(1)
elif x < 0 and y > 0 :
    print(2)
elif x < 0 and y < 0 :
    print(3)
elif x > 0 and y <0 :
    print(4)
else :
    print(0)

x = int(input())
y = int(input())

if (x > 0) & (y > 0) :
    print(1)
elif (x < 0) & (y > 0) :
    print(2)
elif (x < 0) & (y < 0) :
    print(3)
elif (x > 0) & (y <0) :
    print(4)
else :
    print(0)


## 알람
H, M = map(int, input().split())
if M >= 45 :
    print(H, M-45)
elif M <= 44 and H > 0 :
    print(H-1,M+15)
else :
    print(23,M+15)