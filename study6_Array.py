##최소, 최대값 구하기
##Baekjoon 10818번


cnt = int(input())
number = list(map(int,input().split()))
Max = number[0]
Min = number[0]
for i in number[1:]:
    if i > Max :
        Max = i
    elif i < Min :
        Min = i
print(Min, Max)
print(min(number),max(number))

##Baekjoon 2562번
arr = []
for i in range(9) :
    arr.append(int(input()))
max = max(arr)
print(max)
idx = arr.index(max)
print(idx +1)


## Baekjoon 2577번
a = int(input())
b = int(input())
c = int(input())
result = list(str(a*b*c))
for i in range(10):
    print(result.count(str(i))) #i를 문자열(str)로 바꿔서 몇 개있는지 확인
