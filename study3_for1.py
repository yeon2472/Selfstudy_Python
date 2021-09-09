## 구구단
# 숫자 하나 입력받아 그 숫자의 구구단 출력하기
N = int(input())
for i in range(9) :
    i += 1
    print(N, "*", i, "=", N*i)

# 간단 방법2
N = int(input())
for i in range(1,10) :
    print(N,"*",i,"=",N*i)

## 두 정수 입력받아 덧셈
# 모든 값을 입력받고 한꺼번에 출력
T = int(input())
result = [ ]
for i in range(T) :
    A,B = map(int, input().split())
    result.append(A+B)
for i in range(T) :
    print(result[i])

# 방법2 - 방법1과의 차이점은 방법2는 그때그때 출력
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(a+b)

##합
n = int(input())
sum = 0
for i in range(1,n+1) :
    sum = sum + i
print(sum)