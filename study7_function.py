## Baekjoon 15596번_정수 N개의 합
#방법 1
def solve(a) :
    return sum(a)

#방법 2
def solve2(b) :
    ans = 0
    for i in b :
        ans += i
    return ans

## Baekjoon 4673번_셀프 넘버
arr = [ i for i in range(1,10001)]
for i in range(1,10001):
    number = sum(map(int, str(i)))
    if i + number <= 10000 and i+number in arr:
        a = i + number
        arr.remove(a)
for i in range(len(arr)):
    print(arr[i])

## Baekjoon 1065번_한수
#한수: 어떤 양의 정수 X의 각 자리가 등차수열을 이루는 경우
#등차수열: 연속된 두 개의 수 차이가 일정한 수열
n = int(input())
han = 0
for i in range(1, n + 1):
    if i < 100:
        han += 1
    else:
        ns = list(map(int, str(i)))
        if ns[0] - ns[1] == ns[1] - ns[2]:
            han += 1
print(han)
 #1부터 99까지 모두 등차수열
