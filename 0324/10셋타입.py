# set 클래스
# 여러 개의 자료를 비순서로 적재하는 가변길이 비순차 자료구조

# 변수 = {값1, 값2, 값3, ...}
# 특징
# 1) *****중복을 허용하지 않음*****
# 2) 순서가 없기 때문에 색인(index)을 쓸 수 없음
# 3) 객체에서 제공하는 함수를 이용하여 추가, 삭제 및 집합 연산 등이 가능함

# 1) 중복 불가
# set은 자동으로 중복을 제거 => 주로 중복된 원소를 제거하고자 할 때 사용한다
se = {1,2,3,4,1} # => se변수는 set타입 ! 중괄호를 썼다고 해서 딕셔너리 타입은 아니다
print(len(se))  # 4
print(se)       # {1, 2, 3, 4} => 중복이 허용되지 않기 때문에 중복값은 저장되지 않았음
se = {2,3,4,1}
print(len(se))  # 4
print(se)       # {1, 2, 3, 4} => 숫자는 정렬 표시됨 (문자는 안됨)

st = set('hello') # set() : 셋 타입을 생성하는 함수
print(len(st))
print(st)       # {'h', 'e', 'l', 'o'}

# 2) 요소 반복 - set은 색인만 없을 뿐 열거형 자료이기 때문에 for문으로 출력 가능
for d in se:
    print(d,end=' ')    # 1 2 3 4 
print()

for s in st:
    print(s, end=' ')   # h e l o => 숫자는 자동 정렬되어 입력되지만, 문자는 임의로 입력·저장된다
print()

# 3) 집합 관련 함수
# union([set타입 자료]) : 합집합 (중복 제거)
# difference([빼고자 하는 set타입 자료]) : 차집합
# intersection([set타입 자료]) : 교집합
# add(원소값) : 집합에 값을 추가하는 함수
# discard() : 집합에 있는 원소를 제거

se = {1,2,3,4}
se2 = {2,4,6,8}
print(se.union(se2))            # {1, 2, 3, 4, 6, 8}
print(se.difference(se2))       # {1, 3}
print(se.intersection(se2))     # {2, 4}
se.add(7) # 중복이 아닐 경우 값이 추가됨
print(se)                       # {1, 2, 3, 4, 7}
se.discard(3)
print(se)                       # {1, 2, 4, 7}

st = set('hello')
st2 = set('world')  # {'r', 'w', 'd', 'l', 'o'} => 임의의 순서로 입력됨
print(st.union(st2))            # {'r', 'h', 'w', 'd', 'l', 'e', 'o'}
print(st.difference(st2))       # {'h', 'e'}
print(st.intersection(st2))     # {'l', 'o'}
st.add('test')
print(st)  # {'h', 'test', 'l', 'e', 'o'} => 'test'가 원소값으로 입력되었기 때문에 분리되지 않음

# 값의 타입은 상관하지 않는다
lst = ['test','user','server','data']
print(set(lst))     # {'user', 'server', 'data', 'test'} 
                    # => lst의 각 요소들이 원소값 자체로 들어가서 문자열이 분리되지 않음

