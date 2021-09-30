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

## Baekjoon 3052번
#set() : 중복을 제거하기 위한 필터 역할
result = []
for i in range(10) :
    num = int(input())
    result.append(num % 42)
result = set(result)
print(len(result))

##Baekjoon 1546번
N = int(input())
score = list(map(int, input().split()))
max_score = max(score)

new_list = []
for i in score :
    new_list.append(i/max_score * 100)
avg = sum(new_list)/N
print(avg)

## Baekjoon 8958번
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계 리셋
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score
        else:
            score = 0
    print(sum_score)

## Baekjoon 4344번
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  #
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')