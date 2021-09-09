## 빠른 A+B
'''
sys.stdin.readline() 사용법
# sys.stdin.readline : 반복문으로 여러줄을 입력 받아야할 경우 시간문제를 해결할 수 있음
# sys.stdin.readline()은 한줄 단위로 입력받기 때문에 개행문자가 같이 입력받아짐 -> 개행문자 제거해아함
# 한개의 정수를 입력받을 떄
import sys
a = int(sys.stdin.readline())

#정해진 개수의 정수 한줄에 입력받을 떄
import sys
a,b,c = map(int, sys.stdin.readline().split())

#임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 떄
import sys
data = list(map(int, sys.stdin.readline().split()))

#문자열 n줄을 입력받아 리스트에 저장할 때
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)] #strip(): 문자열 맨 앞, 끝의 공백문자 제거
'''

#baekjoon_15552_for문, 빠른 A+B
import sys
T = int(input())
for i in range(T) :
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)

#baekjoon_2714_for문_자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하기
N = int(input())
for i in range(N) :
    i = i+1
    print(i)



#baekjoon_11021_for문_두 정수 A,B 입력받은 다음, A+B 출력하기
T = int(input())
for i in range(T) :
    A,B = map(int, input().split())
    print("Case #",i+1,": ",A+B,sep="")

#baekjoon_2438_for문_별 N개 찍기
N = int(input())
for i in range(N) :
    i += 1
    for k in range(i) :
        print("*",sep="",end="")
    print()
# 2(더 짧은 코드)
N = int(input())
for i in range(1, N+1) :
    print('*'*i)

#baekjoon_2439_for문_별 N개 찍기(오른쪽 기준정렬)
n = int(input())
for i in range(1, n+1) :
    print(" "*(n-i),"*"*i, sep="")


#baekjoon_10871_for문_수열 A와 정수 X, A에서 X보다 작은 수 모두 출력
N,X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    if i < X :
        print(i, end=" ")