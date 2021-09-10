## while문 학습
## Baekjon_10952_두 정수 A+B
while True :
    A,B = map(int, input().split())
    if A == 0 & B == 0 :
        break
    print(A + B)


## Baekjon_1110_더하기 사이클
N = int(input())
num = N
count = 0
while True :
    count += 1
    temp = num//10 + num%10
    new_N = (num%10)*10 + temp%10
    if N == new_N:
        break
    num = new_N
print(count)

## Baekjon_ 10951_try, except
while True:
    try :
        A,B = map(int,input().split())
        print(A+B)
    except :
        break