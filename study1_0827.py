#사칙연산
# 숫자 입력받고 계산 결과 출력하기
# 주의사항: input할 땐 str이므로 int해주는거 잊지말기
# 여러 값을 한줄로 입력받을 땐 split으로 띄어쓰기 구분해주기
#값 입력받을 때 방법
#1

A,B = map(int, input().split())
print(A,B)
#2
A,B = input().split()
print(int(A), int(B))

#A+B 계산 방법
# case1
A, B = input().split()
print(type(A))
print(int(A)+int(B))
# case2
print(eval('+'.join(input())))

#A,B 사칙연산
# 나누기 몫은 / 로 구할 수 있으나 실수로 나옴, 정수형이 나오게 하려면 // 두개 사용(+int형)
A,B = input().split()
print(int(A)+int(B))
print(int(A)-int(B))
print(int(A)*int(B))
print(int(A)//int(B))
print(int(A)%int(B))

A,B = map(int, input().split())
out1 = A*(B%10)
out2 = A*((B%100)//10)
out3 = A*(B//100)
res = A*B
print(out1, out2, out3, res, sep="\n")

# case 2
a,b=map(int,open(0))
print(b%10*a, b%100//10*a, b//100*a, b*a)

# case 3
A = int(input())
B = input()
print(int(B[2]))
print(int(B[1]))
print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))
