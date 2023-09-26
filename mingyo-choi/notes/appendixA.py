#1. List
a = [1, 2, 3, 4, 5]
print(a)
print(a[3])

##빈 리스트 생성
a = list()
print(a)

##크기가 n이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

##리스트 초기화 연습
b = []
for i in range(4, 10): #4이상 10미만
  if i % 2 == 0 :
    b.append(i)
print(b)

###주의 : 리스트 컴프리헨션
k = [i for i in range(4, 10) if i % 2 == 0]
print(k)

x = [i**2 for i in range(1, 10) ]
print(x)

n = 3
m = 4 #n*m크기 2차원 초기화
# _ : 반복위한 변수! 굳이st.. for _ in range(5) print 어쩌구와 비슷한 맥락
array = [[0]*m for _ in range(n)] 
print(array)

test = [[0] * m] * n
print('test: ', test)
test[1][1] = 5
print(test)

test = [[0] * m for _ in range(n)]
print('test: ', test)
test[1][1] = 5
print(test)


##리스트 인덱싱
a = []
for i in range(1,11):
  a.append(i)
print(a[-1])
a[3] = 100
print(a)

##리스트 슬라이싱
print(a[1:4]) #인덱스1이상 4미만으로 잘림

##기타 리스트 매서드
a = [1, 4, 3]
a.append(2)
print(a)
a.sort()
print('sorted: ', a)
a.sort(reverse=True)
print('reverse sorted: ', a)
a.reverse()
print('re: ', a)
a.insert(2, 300) #느림
a.insert(2, 400)
a.insert(2, 300)
a.insert(2, 500)

print(a)
print('값이 300인 데이터 수: ', a.count(300))

a.remove(300) #앞에서부터 지우네 얘도 느림
print(a)

a = [1, 2, 3, 4, 5, 5, 5, 5]
remove_set = {1, 5}
result = [i for i in a if i not in remove_set]
print(result)

#2. Tuple
#리스트와 비슷하지만, 한 번 선언된 값을 변경할 수 없음. 소괄호
#그래프 알고리즘에 자주 사용 - 우선순위 큐 등
#리스트보다 공간효율적
#서로 다른 성질의 데이터 묶어서 관리 - (비용, 노드번호) 등

#3. Dictionary
x = dict()
x['사과'] = '애플'
x['배'] = '피어'
x['자두'] = '플럼'
print(x)
if '사과' in x:
  print('있음')
x_key_list = x.keys()
x_val_list = x.values()
print(x_key_list, x_val_list)
for key in x_key_list:
  print(key)

#4. Set
#중복 비허용, 순서x -> 인덱싱 불가
#합집합 | 차집합 - 교집합 &
a = set([1,1,2])
print(a)
a = {1, 1, 2, 3}
print(a)
a.add(4)
print(a)
a.update([7,5,9,3])
print(a)
a.remove(5)
print(a)

#조건문

x = 70
if x>=10 :
  print('hi')

if x>=90 :
  print('A')
elif x>=80 :
  print('B')
elif x>=70 :
  print('C')
else :
  print('F')

score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 4}

result = []
for i in a :
  if i not in remove_set :
    result.append(i)

print(result)

hehe = [i for i in a if i not in remove_set]
print(hehe)

x = 10
if 9<x<11 :
  print('good')


#반복문

i = 1
result = 0
while i <= 9:
  result += i
  i += 1

print(result)

i = 1
result = 0
while i <= 9 :
  if i%2 == 1 :
    result += i
  i += 1

print(result)

result = 0
for i in range(1, 10) :
  result += i
print(result)

scores = [90, 85, 77, 65, 97]
for i in range(5):
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격티비")

for i in range(2, 10):
  for k in range (1, 10):
    print(i, "X", k, "=", i*k)

#함수

def add(a, b):
  print('함수의 결과: ', a+b)

add(20, 9)

def add(a, b):
  print('함수의 결과: ', a+b)

add(a=3, b=7)

a = 0
def func():
  global a
  a+=1

for i in range(10):
  func()

print(a)

def add(a, b):
  return a+b
print(add(3, 7))


print((lambda x, y: x**y)(3, 3))



#입출력
list(map(int, input().split()))
list(map(int, input().split())) #일단 인풋을 스플릿해서 리스트에 넣는데, 이걸 다시 정수형으로 바꿔줘야함
#map은 반복 적용

##전형적인 코드
n = int(input()) 
#인풋받고 정수형으로 바꿔서 n에 집어넣기 -> 입력받을 데이터 수

data = list(map(int, input().split()))
data.sort(reverse = True) #내림차순 정렬
print(data)

#적은 수의 데이터 입력
n, m, k = map (int, input().split())
print('n: ',n, 'm: ', m, 'k: ', k)


#입력 개수 많은 경우!! 시간 초과 고려
#rstrip() : 공백문자 (엔터) 제거
import sys
data = sys.stdin.readline().rstrip()
print(data)
import sys
data = sys.stdin.readline().rstrip()

import sys
data = sys.stdin.readline().rstrip()


a=1
b=2
print(a,b)
#문자열은 +로 연결가능
answer = 7
print('답은 ',answer, '입니다') #,사용하면 의도치 않은 띄어쓰기

answer = 10
print(f"정답은 {answer}입니다") #f-string

#주요 라이브러리
'''
1. 내장함수: print(), input()과 같은 기본 입출력 ~ sorted()와 같은 정렬 포함한 기본 내장 라이브러리
2. itertools: 파이썬에서 >>반복되는 형태의 데이터<<를 처리하는 기능을 제공하는 라이브러리! 순열, 조합 라이브러리 제공
3. heapq: 힙 기능 제공 for 우선순위 큐 기능 구현
4. bisect: 이진 탐색
5. collections: 덱, 카운터 등의 자료구조 포함한 라이브러리
6. math: 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련, 파이(pi) 등의 상수까지..
'''

#1. 내장함수: import 없이 바로 사용
result = sum([1, 2, 3, 4, 5])
print(result)

result = min([3, 7, -1])
print(result)

result = max([400, 324, 232, 329])
print(result)

result = eval("3*(4+5)-10")
print(result)

result = sorted([2,4,1,30,22, 40])
print(result)
result = sorted([2,302,49238,439201,293,2834], reverse=True)
print(result)

result = sorted([('홍길동', 35), ('김순신', 75), ('아무개', 40)], key = lambda x: x[0], reverse=True)
print(result)

data = [9, 2, 4, 5, 1, 2]
data.sort()
print(data)
data.sort(reverse=True)
print(data)

#2. itertools
from itertools import permutations #순서나열
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

from itertools import combinations #뽑기
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)
result = list(permutations(data, 2))
print(result)
result = list(combinations(data, 3))
print(result)

#중복 포함 뽑아서 나열
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

#중복 포함 뽑기
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)

#3. heapq -> 우선순위 큐 기능
#삽입: heapq.heappush()
#꺼내기: heapq.heappop()

#힙정렬
import heapq
def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h, value) #힙 h에다가 value를 차례로 삽입
  for i in range(len(h)):
    result.append(heapq.heappop(h)) #힙 h에 담긴 것들을 하나씩 빼담기
  return result

a = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(a)

import heapq
def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h, -value)
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


#4. bisect -> 정렬된 배열에서 특정 원소 찾을 때
#bisect_left(a, x) : 리스트 a에 데이터 x 삽입할 가장 왼쪽 인덱스 찾기
#bisect_right(a, x) : 리스트 a에 데이터 x 삽입할 가장 오른쪽 인덱스 찾기

from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

#정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수
#count_by_range(a, left_value, right_value)

from bisect import bisect_left, bisect_right
def count_by_range(a, left_val, right_val):
  right_index = bisect_right(a, right_val)
  left_index = bisect_left(a, left_val)
  return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

#5. collections
#deque : 인덱싱, 슬라이싱은 x 그러나 시작부분이나 끝 부분에 삽입삭제 굿
#첫 원소 제거: popleft(), 첫 인덱스에 x 삽입: appendleft(x)
#마지막 원소 제거: pop(), 마지막 인덱스에 x 삽입: append(x)
#deque를 통해 큐 자료구조 - 삽입은 append(), 삭제는 popleft()

from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))


#Counter: 등장 횟수 세기
from collections import Counter
counter = Counter(['red', 'blue', 'green', 'red', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))


import math 
print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21, 14))
print(math.pi)
print(math.e)

















