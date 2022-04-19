# count 특정 값의 개수를 출력
lst1 = [1,2,3,2,5,6,2,8]
su = lst1.count(2)
print(lst1)
print("2의 값을 가진 멤버의 개수 :", su)    # 2의 값을 가진 멤버의 개수 : 3

# index(value) : 특정 값의 인덱스값을 반환 - 못찾으면 ValueError
lst1 = [1,2,3,2,5,6,2,8]
# (+)   0 1 2 3 4 5 6 7
idx = lst1.index(5)             
print("5의 idx값을 확인 :",idx)    # 5의 idx값을 확인 : 4 
idx = lst1.index(2,2)             # 값 2에 대해 index=2인 3부터 찾음
print("2의 idx값을 확인 :",idx)     # 2의 idx값을 확인 : 3 

# reverse() : 리스트 멤버의 순서를 반전 (정렬은 아님)
lst1 = [9,10,3,2,6,1,7,8,4,5]
print("reverse() 사용 전 :",lst1)   # [9, 10, 3, 2, 6, 1, 7, 8, 4, 5]
lst1.reverse()
print("reverse() 사용 후 :",lst1)   # [5, 4, 8, 7, 1, 6, 2, 3, 10, 9]

# sort() : 리스트를 정렬하는 함수
#   - 오름차순(작은 -> 큰) => reverse=False (기본값)
#   - 내림차순(큰 -> 작은) => reverse=True
lst1 = [9,10,3,2,6,1,7,8,4,5]
lst1.sort()                 # 오름차순 정렬
print(lst1)              # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst1.sort(reverse=True)     # 내림차순 정렬
print(lst1)              # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# sort 사용 시 주의사항
# 1. 숫자 형식 또는 문자 형식은 분리해서 정렬해야 함 (정렬이 필요하면 숫자형식이나 문자형식으로 자료형을 통일하기)
# 2. 정수와 실수는 같은 숫자이기 때문에 정렬 가능

# sorted() 함수 : 정렬된 리스트를 새롭게 만들고 싶은 경우 사용 
lst1 = [9,10,3,2,6,1,7,8,4,5]
lst2 = sorted(lst1)     # sorted 함수는 기존 리스트는 변경시키지 않고, 새로운 리스트에 정렬하여 대입함
print(lst1, id(lst1))   # [9, 10, 3, 2, 6, 1, 7, 8, 4, 5] 2497653433472
print(lst2, id(lst2))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 2497653428096

lst3 = sorted("I am a student".split(' '))     # 문자의 아스키코드 순서대로 정렬함 (대문자는 소문자보다 아스키코드가 작음!)
print(lst3)     # ['student', 'am', 'a', 'I']

lst4 = sorted("I am a student".split(),key=str.lower) # upper(대문자), lower(소문자) => 전체를 대문자 or 소문자로 취급하여 대소문자 구별없이 정렬
print(lst4)     # ['a', 'am', 'I', 'student']

# ** split() 문자열을 분리하는 함수
# ()안에 인자값을 아무것도 넣지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나눠서 사용함
# ex) split(';')을 사용하면 ';'을 기준으로 문자열을 나누겠다는 의미

# copy 기능
# shallow copy : 서로 다른 변수가 같은 위치에 있는 데이터를 가리키는 경우
# deep copy : 두 개의 변수가 별도의 공간을 가리키는 경우

# 예) shallow copy - 데이터를 참조하는 형태로 복사 => 참조하는 주소(id)가 동일함
lst1 = [1,2,3,4,5]
lst2 = lst1
print("lst1의 값 :",lst1,"\tlst1의 주소 값 :",id(lst1))
print("lst2의 값 :",lst2,"\tlst2의 주소 값 :",id(lst2))

lst1[1] = 'a'      # lst2가 lst1의 값을 참조하고 있기 때문에 lst1이 변경되면 lst2도 변경된다
print("lst1의 값 :",lst1,"\tlst1의 주소 값 :",id(lst1))
print("lst2의 값 :",lst2,"\tlst2의 주소 값 :",id(lst2))

# 예) deep copy - 데이터 자체를 복사 => 값은 같으나 참조하는 주소(id)는 상이함
lst1 = [1,2,3,4,5]
lst2 = list(lst1)   # list()는 새로운 리스트를 생성하는 메서드
lst1[1] = 'a'
print(lst1, id(lst1))   # [1, 'a', 3, 4, 5] 2497689998080
print(lst2, id(lst2))   # [1, 2, 3, 4, 5] 2497689995520

# 복사 기능을 제공하는 copy 모듈을 불러서 사용
import copy
lst1 = [1,2,3,4,5]
lst2 = copy.deepcopy(lst1)  # deepcopy() => 데이터는 같으나 주소(id)는 다름
print(lst1, id(lst1))   # [1, 2, 3, 4, 5] 2497690031360
print(lst2, id(lst2))   # [1, 2, 3, 4, 5] 2497690033024

lst3 = lst1                 # shallow copy
print(lst1, id(lst1))   # [1, 2, 3, 4, 5] 2497690031360
print(lst3, id(lst3))   # [1, 2, 3, 4, 5] 2497690031360

# [Quiz 1] : 리스트 초기값 설정 후 메서드를 사용하여 출력하기
lst = [30,20,10]
print("현재 리스트 :",lst)                      # 현재 리스트 : [30, 20, 10]
lst.append(40)
print("append(40) 후의 리스트 :",lst)           # append(40) 후의 리스트 : [30, 20, 10, 40]
print("pop()으로 추출한 값 :",lst.pop(3))       # pop()으로 추출한 값 : 40
print("pop() 후의 리스트 :",lst)                # pop() 후의 리스트 : [30, 20, 10]
lst.sort()
print("sort() 후의 리스트 :",lst)               # sort() 후의 리스트 : [10, 20, 30]
lst.reverse()
print("reverse() 후의 리스트 :",lst)            # reverse() 후의 리스트 : [30, 20, 10]

# [Quiz2] : 리스트 초기값 [30,20,10] 설정 후 코드 작성
lst = [30,20,10]
print("현재 리스트 :",lst)                          # 현재 리스트 : [30, 20, 10]
print("10의 값의 위치 :",lst.index(10))             # 10의 값의 위치 : 2
lst.insert(2, 200)
print("insert(2,200) 후의 리스트 :",lst)            # insert(2,200) 후의 리스트 : [30, 20, 200, 10]
lst.remove(200)
print("remove(200) 후의 리스트 :",lst)              # remove(200) 후의 리스트 : [30, 20, 10]
lst.extend([555,666,555])
print("extend([555,666,555]) 후의 리스트 :",lst)    # extend([555,666,555]) 후의 리스트 : [30, 20, 10, 555, 666, 555]
print("555 값의 개수 :",lst.count(555))             # 555 값의 개수 : 2


# 2차(원) 리스트 : 리스트 안의 멤버 중에 리스트가 존재하는 경우 사용되는 방식
# 리스트 안에 있는 리스트 멤버에 대한 참조 방식

# 예제1) 2차 리스트 변수 값 참조 - 이중for문으로 멤버리스트의 값을 읽음
aa = [  [1,2,3,4],      # aa[0]
        [5,6,7,8],      # aa[1]
        [9,10,11,12] ]  # aa[2]    
print(len(aa))      # aa 리스트의 멤버 개수 : 3
print(aa)           # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

for x in range(len(aa)) :           # aa리스트의 멤버 수
    for y in range(len(aa[x])) :    # aa의 멤버리스트의 멤버개수
        print(aa[x][y], end='\t')
    print()
    

# 예제2) 2차 리스트 생성 및 출력
ls_1 = []; ls_2 = []; value = 1
# 2차 리스트 생성
for i in range(3) :         # 상위 리스트의 멤버 개수 (행)
    for j in range(4) :     # 하위 멤버리스트의 멤버 개수 (열)
        ls_1.append(value)
        value += 1
        # i=1 => ls_1 = [1,2,3,4]
        # i=2 => ls_1 = [5,6,7,8]
        # i=3 => ls_1 = [9,10,11,12]        
    ls_2.append(ls_1)       # for j문에서 만들어진 리스트가 추가됨
    ls_1 = []               # ls_1 초기화 -> clear로 비우게 되면 ls_2의 값도 변경됨 ㅠㅠ
                            

print(ls_1)     # []
print(ls_2)     # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

#초기화하지 않으면 마지막 ls_1의 값으로 모든 행이 채워지게 됨
# ls_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# ls_2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]

# 출력(읽기)
for x in range(len(ls_2)) :
    for y in range(len(ls_2[x])) :
        print(ls_2[x][y], end='\t')
    print()
    

# [문제1] numbers = [10,20,30,40,50,60,70]
# 위 리스트의 모든 값을 더한 결과를 출력하세요
numbers = [10,20,30,40,50,60,70]
sum = 0
for x in range(len(numbers)) :
    sum += numbers[x]
print(sum)

# [문제2] 1~45까지의 임의의 값을 중복 없이 6개 생성하여 출력
from random import randint
rnds = []
while len(rnds) <= 6 :
    num = randint(1, 45)
    for x in rnds :
        if num == x :
            num = randint(1, 45)
            continue
    rnds.append(num)
print(rnds)

# 선생님 답 ㅠㅠㅠㅠㅠ
lotto = []
while len(lotto) <= 6 :
    num = randint(1, 45)
    if num not in lotto :    # 리스트가 있는 경우 파이썬의 특성을 꼭 기억해서 반복문/제어문 코드짜기 !!!
        lotto.append(num)
lotto.sort()
print(lotto)

# [문제3] lst_sec = [['홍길동','남',36],['김수양','여',32],['박담수','남',28]]
# 위의 2차 리스트 자료를 다음과 같은 형식으로 출력
# 이름 : 홍길동
# 성별 : 남
# 나이 : 36
lst_sec = [['홍길동','남',36],['김수양','여',32],['박담수','남',28]]
for x in range(len(lst_sec)) :
    for y in range(len(lst_sec[x])) :
        if y == 0 :
            print("이름 :",lst_sec[x][y])
        elif y == 1 :
            print("성별 :",lst_sec[x][y])
        elif y == 2 :
            print("나이 :",lst_sec[x][y])
# 선생님 답 ㅠㅠㅠㅠ!!!!!!!!!!!
for val in lst_sec :
    print(f"이름 : {val[0]}")
    print(f"성별 : {val[1]}")
    print(f"나이 : {val[2]}")
    print()

# [문제4] 구구단을 출력하는 코드를 작성하되, 2차 리스트에 결과값을 저장하고 출력할 수 있도록 하시오
table=[]; times=[]
for x in range(2,10) :
    for y in range(2,10) :
        times.append("{} x {} = {}".format(x,y,x*y))
    table.append(times)
    times=[]

for x in range(len(table)) :
    print(table[x])

# 선생님 답
gugu = []
for x in range(2,10) :
    gugu.append([])
    for y in range(1,10) :
        gugu[x-2].append(x*y)

for x in range(2,10) :
    for y in range(1,10) :
        print("{} x {} = {:<3}".format(x,y,gugu[x-2][y-1]), end="")
    print()


# list 내포(List Comprehension) : 리스트 안에서 for와 if를 사용하는 문법

x = [2,4,1,5,7]     # 각 멤버를 제곱승으로 처리
# 예시) 지금까지 배운대로
lst = []
for i in x:
    i **= 2
    lst.append(i)
print(lst)

# 형식 1 (for) ===============================================================
# 변수 = [실행문 for 변수 in 열거형객체]
#       * for문의 실행 결과가 변수 리스트에 append 처리됨
lst1 = [i**2 for i in x]       # x(=열거형 자료(list))의 멤버들을 **2한 처리 결과로 append
print(lst1)

# 형식 2 (for + if) ==========================================================
# 변수 = [실행문 for 변수 in 열거형객체 if 조건문]
# 1~10 -> 2의 배수 추출 -> i * 2 -> list에 저장
num = list(range(1,11)) # num = [1,2,3,4,5,6,7,8,9,10]
lst2 = [i*2 for i in num if i % 2 == 0]     # 조건에 부합하는 값만 연산하여 리스트에 넣음 - 조건에 부합하지 않으면 새 리스트에 추가되지 않음
print(lst2)     # [4, 8, 12, 16, 20]


# [프로그래밍 문제]
# 아래와 같은 메뉴를 만들고, 친구 이름을 관리하는 코드 작성 - 리스트를 사용해서 작성
'''
1. 친구 리스트 출력     # 등록한 친구 목록 보기 기능
2. 친구 추가            # 친구 등록하기(정보는 문제3번 참조) 기능
3. 친구 삭제            # 등록 친구 삭제 기능
4. 이름 변경            # 이름 변경 기능
0. 종료                # 프로그램 종료
메뉴를 선택하세요 : 2
이름을 입력하시오 : 홍길동
'''
import os
friends = []; menu=1
while menu != 0 :
    os.system('cls')
    print("="*30)
    print("1. 친구 리스트 출력\n2. 친구 추가\n3. 친구 삭제\n4. 이름 변경\n0. 종료")
    menu = int(input("메뉴를 선택하세요 : "))
    if menu == 1 :
        for x in friends :
            print("이름 :",x[0],end=' / ')
            print("성별 :",x[1],end=' / ')
            print("나이 :",x[2])
        os.system('pause')
    elif menu == 2 :
        name = input("친구의 이름을 입력하세요 : ")
        gender = input("친구의 성별을 입력하세요(남/여) : ")
        age = int(input("친구의 나이를 입력하세요 : "))
        friends.append([name,gender,age])
        os.system('pause')
    elif menu == 3 :
        name = input("삭제할 친구의 이름을 입력하세요 : ")
        for x in friends :
            if x[0] == name :
                friends.pop(friends.index(x))
            else : print("해당 이름은 친구목록에 존재하지 않습니다")
        os.system('pause')
    elif menu == 4 :
        old = input("변경할 친구의 이름을 입력하세요 : ")
        for x in friends :
            if x[0] == old : x[0] = input("변경할 이름을 입력하세요 : ")
            else : print("해당 이름은 친구목록에 존재하지 않습니다")
        os.system('pause')