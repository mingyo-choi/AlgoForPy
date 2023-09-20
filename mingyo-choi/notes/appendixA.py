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
