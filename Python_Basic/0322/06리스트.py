'''
LIST 리스트 자료형
    - 데이터 목록을 다루는 자료형
    - 리스트를 정의할 때는 "[]"를 사용함
    - 리스트 안에는 어떤 종류의 자료형이든 상관없이 저장 가능
    
List 자료형의 기본 사용(정의)

<정의>
    변수명 = []     # 비어있는 리스트를 선언
    변수명 = [value1, value2, value3, value4 ...]   # value 자료 타입은 상관없이 선언 가능

<list()를 이용한 리스트 생성>
    변수명 = list()         # 비어있는 리스트 선언
    변수명 = list("Hello)   # ['H','e','l','l','o']
    변수명 = list(range(5)) # [0,1,2,3,4]
'''

# 예제1) 리스트 선언 및 값에 대한 처리
list = [1,2,3,4,5,6,7,8]
print(type(list))   # <class 'list'>
# 생성된 리스트에 대한 특정 값 참조 : 인덱스(index)값을 이용
# 인덱싱 방법 : 변수명[인덱스값]    -> 인덱스값의 시작은 0부터 !!
print(list[0])      # 1
print(list[3])      # 4
# 인덱싱을 이용한 list값 변경
list[0] = list[5]
print(list[0])
print(list)     # [6, 2, 3, 4, 5, 6, 7, 8]

# 리스트 자료의 길이 (요소(멤버)의 개수) : len()
print("list1의 길이 :",len(list1))

# 리스트의 결합 1 - 병합
list2 = [9,10]          # list1의 길이 : 8
print(list1+list2)      # [6, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list3 = list1 + list2
print(list3)            # [6, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트의 결합 2 - 확장
list1 = list1 + list2
print(list1)            # [6, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트의 반복
print(list2 * 3)        # [9, 10, 9, 10, 9, 10]

# max() : 최대값, min() : 최소값            * abs():절대값처리 / pow(base,exp) : base의 exp제곱 구하기
# list1 = [6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 10]
print(max(list1))
print(min(list1))
print(sum(list1))

# 파이썬에서는 list를 변수로 사용한다 - list자료형으로 전달하고자 하는 변수를 모두 묶어서 전달 가능!

# 예시) 변수를 선언, 3개의 정수를 입력 받아 합을 출력하기 / 출력결과 >> "합계" = xx / "합계" 문자도 변수로 저장하기
nums = [] ; x=0; sum=0
for x in range(3) :
    num = int(input("정수를 입력해주세요 >>> "))
    nums.append(num)
    sum += num
nums.append("합계 =")
nums.append(sum)
print(nums[3],nums[4])

# 쌤 답안
a = int(input("첫 번째 정수를 입력해주세요 >>> "))
b = int(input("두 번째 정수를 입력해주세요 >>> "))
c = int(input("세 번째 정수를 입력해주세요 >>> "))
d = "합계"
sum = a+b+c
print(f"{d}={sum}")

# List 인덱싱 : 인덱스 값을 이용한 참조     
# lst = [1,2,3,4,5,6,7,8]
# 양의 index :  0  1  2  3  4  5  6  7
# 음의 index : -8 -7 -6 -5 -4 -3 -2 -1
#   * -1을 bit값으로 표시하면 : 11111111 11111111 11111111 11111111
#   * -2를 bit값으로 표시하면 : 11111111 11111111 11111111 11111110
# 예시3) list인덱싱
lst = [1,2,3,4,5,6,7,8]
# (+)  0  1  2  3  4  5  6  7
# (-) -8 -7 -6 -5 -4 -3 -2 -1
print("lst[] : ",lst)
print("lst[-1] : ",lst[-1])     # 8
print("lst[-2] : ",lst[-2])     # 7
print("lst[-3] : ",lst[-3])     # 6

# slicing 방식을 이용한 시퀀스 객체(자료) 접근
# slicing이란 ? 리스트와 같은 시퀀스 자료 값들의 범위로 접근하기 위해 사용하는 방법 - 시퀀스 자료의 일부를 잘라서 새롭게 생성하는 것
#(형식)
#   변수명[시작인덱스:끝인덱스]
#   변수명[시작인덱스:끝인덱스:증감값]
# 예시) lst = [1, 2, 3, 4, 5, 6]
#     index   0  1  2  3  4  5
#      (-)   -6 -5 -4 -3 -2 -1
lst = [1, 2, 3, 4, 5, 6]
print(lst[0:3])         # [1, 2, 3]
print(lst[0:3:2])       # [1, 3]
print(lst[-6:-3])       # [1, 2, 3]
print(lst[-1:-3:-1])    # [6, 5] - 역순으로 출력 
print(lst[5:0:-3])      # [6, 3]

# 인덱스 생략
lst = [1, 2, 3, 4, 5, 6]
print(lst[:3])    # 시작값 생략 - [1, 2, 3] 
print(lst[3:])    # 끝값 생략 - [4, 5, 6]
print(lst[:])     # 둘 다 생략 - [1, 2, 3, 4, 5, 6]

# 슬라이싱 후 새로운 리스트 생성
slc1 = lst[3:6]
print(slc1)         # [4, 5, 6]
slc2 = lst[1:5:3]
print(slc2)         # [2, 5]
slc3 = lst[5::-1]
print(slc3)         # [6, 5, 4, 3, 2, 1]
slc4 = lst[-3:-1]
print(slc4)         # [4, 5]


# 리스트 함수들

# ============== 값 추가 메서드 ==============
# append(value) : 리스트 끝에 값을 추가(멤버 추가)
# extend(iter) : 리스트 끝에 list, tuple, dict의 값을 하나씩 추가
# insert(idx, value) : 특정 인덱스 위치인 idx에 특정 값을 추가
#                      지정한 인덱스에 자료가 있다면 해당 인덱스에 추가 후 이후 자료의 인덱스가 하나씩 밀려남

# ============== 값 삭제 메서드 ==============
# pop([idx]) : 인덱스를 지정하지 않으면 마지막 인덱스 값을 반환 후 삭제
#              인덱스 값을 지정하면 해당 인덱스 값을 반환 후 삭제
# remove(value) : 특정 값을 찾아서 삭제하는 함수
# clear() : 리스트의 모든 멤버를 삭제하고 빈 리스트로 만드는 함수

# ============== 기타 메서드 ==============
# count(value) : 리스트 내에 특정 값의 개수를 반환하는 함수
# index(value) : 리스트 내에 특정 값의 인덱스 값을 반환하는 함수
# reverse() : 리스트의 멤버들을 역순으로 나열하는 함수
# sort([reverse=False]) : 리스트의 값을 오름차순(False), 내림차순(True)으로 정렬해주는 함수

print(help('list'))

#append() : 리스트의 끝에 값을 추가
lst1 = [1,2,3,4,5,6,7,8]
lst1.append('a')
print(lst1)
lst1.append([9,10]) # => append를 사용하게 되면 그 자체를 한 인덱스의 자료값으로 넣게 됨
print(lst1)         # [1, 2, 3, 4, 5, 6, 7, 8, 'a', [9, 10]]
print(lst1[-1])     # [9, 10]

# extend() : 리스트 끝에 list, tuple, dict을 하나씩 추가
lst1 = [1,2,3,4,5,6,7,8]
lst1.extend('abcdef') # => append와 달리 한 인덱스에 하나씩 자료값으로 넣게 됨
print(lst1)      # [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', 'd', 'e', 'f']

# insert(idx, value) : idx위치에 값을 추가
lst1 = [1,2,3,4,5,6,7,8]
# idx : 0 1 2 3 4 5 6 7
lst1.insert(3, 'a')
print(lst1)     # [1, 2, 3, 'a', 4, 5, 6, 7, 8] => 기존값들은 밀려남

# pop() : 맨 뒤에 있는 멤버 반환 후 삭제 / 인덱스값을 넣으면 해당 인덱스 값을 반환 후 삭제
lst1 = [1,2,3,4,5]
a = lst1.pop()
print(a)        # 5
print(lst1)     # [1, 2, 3, 4]
b = lst1.pop(2)
print(b)        # 3
print(lst1)     # [1, 2, 4]

# remove(value) : value에 있는 내용을 검색 후 삭제 - 검색값이 없으면 Error를 반환
lst1 = [1,2,3,2,5,6,2,8]
lst1.remove(2)  # 첫 번째 2 삭제
print(lst1)         # [1, 3, 2, 5, 6, 2, 8]
lst1.remove(2)  # 두 번째 2 삭제
print(lst1)         # [1, 3, 5, 6, 2, 8]
lst1.remove(2)  # 세 번째 2 삭제
print(lst1)         # [1, 3, 5, 6, 8]
# lst1.remove(2) 재시도 시 => ValueError : list.remove(x) : x not in list // 메서드 오류 발생

# clear()
lst1 = [1,2,3,4,5]
lst1.clear()
print(lst1)     # []