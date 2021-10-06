##Baekjoon_11654번_아스키 코드
# 알파벳 소문자, 대문자, 숫자0-9중 하나가 주어졌을 떄, 주어진 글자의 아스키 코드값을 출력하는 프로그램
a = input()
print(ord(a))
#ord(): 문자의 아스키 코드값을 리턴하는 함수
#chr(): 아스키 코드값 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수

##Baekjoon_11720_숫자의 합
#N개의 숫자가 공백 없이 쓰여있음, 이 숫자 모두 합해서 출력
# case 1
n = input()
print(sum(map(int,input())))

# case 2
n2 = input()
nums = input()
total = 0
for i in nums :
    total += int(i)
print(total)

##Baekjoon_10809번_알파벳 찾기
#알파벳 소문자로만 이루어진 단어 S가 주어진다.
#각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성
word = input()
alphabet = list(range(97,123))
for i in alphabet :
    print(word.find(chr(i)))

##Baekjoon_2675번_문자열 반복
#문자열 S를 입력받은 후에 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
n = int(input())
for i in range(n) :
    cnt, word = input().split()
    for x in word:
        print(x * int(cnt), end='')
    print()

##Baekjoon_1157번_단어공부
#알파벳 대소문자로된 단어가 주어지면 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램
#대소문자 구분X
# case 1
n = input().upper()
t=[]
for i in set(n) :
    t.append(n.count(i))
idx = [i for i, x in enumerate(t) if x==max(t)]
if len(idx) >1 :
    print("?")
else :
    print(list(set(n))[t.index(max(t))])

# case 2
words = input().upper()
unique_words = list(set(words))

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) >1 :
    print("?")
else :
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])