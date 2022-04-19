# 튜플(tuple) : 리스트와 비슷한 자료형으로 튜플 안에 다양한 형태의 값을 사용할 수 있음
#       (형식)
#       튜플 변수명 = (value1, value2, value3,...)
# 리스트와 튜플의 차이점
# 1. 리스트는 "[]"를 사용하지만, 튜플은 "()"을 사용한다
# 2. 리스트는 그 값을 생성, 삭제, 수정이 가능하지만 튜플은 값을 바꿀 수 없다!!!!!!
#            => 값이 변경되지 않아야 할 때 쓰임
# 3. 튜플은 멤버(요소)의 값이 1개인 경우 반드시 뒤에 ","를 붙여야 한다
#    ex) tu = (1,) => O / tu = (1) => X
# 4. 튜플은 가장 외곽에 있는 "()"는 생략이 가능하다
#    ex) tu = 10,20,30

# 튜플의 인덱싱 : 튜플도 리스트와 같이 인덱싱을 통해 값에 접근
# 예시)
#    튜플      (1, 2, 3, 4, 5, 6, 7, 8, 9)
# 인덱스 값 (+)  0  1  2  3  4  5  6  7  8
# 인덱스 값 (-) -9 -8 -7 -6 -5 -4 -3 -2 -1

# 튜플의 슬라이싱(slicing) : 튜플의 특정 범위의 값에 접근하기 위한 방법으로, 리스트와 동일하게 사용

# 튜플의 정의 및 사용
tu = (1,2,3,4,5,6,7,8,9)
print(tu, type(tu))     # (1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'tuple'>
print(tu[0])            # 1
print(tu[4])            # 5
print(tu[-2])           # 8
print(tu[:3])           # (1, 2, 3)
print(tu[5:])           # (6, 7, 8, 9)

tu1 = '문자열',100,123.456 # => 가장 외곽의 괄호 생략 가능
print(tu1, type(tu1))       # ('문자열', 100, 123.456) <class 'tuple'>
tu2 = (10)
print(tu2, type(tu2))       # 10 <class 'int'> => 괄호로 묶었다고 해서 튜플이 아님
tu3 = (10,)
print(tu3, type(tu3))       # (10,) <class 'tuple'> => 리스트와 튜플 차이점 3번 참고
tu4 = 10,
print(tu4, type(tu4))       # (10,) <class 'tuple'> => 가장 외곽의 괄호 생략 가능

# 예제 2) 튜플의 특정
tu = (1,2,3,4,5)
# tu[0] = 100 # => TypeError - 한 번 정의된 튜플은 멤버의 값을 변경할 수 없다 (split은 가능)

# 예제 3) 튜플의 결합1 - 병합
a = 1,2,3
b = 4,5,6
c = a + b
print(c)            # (1, 2, 3, 4, 5, 6)

# 예제 4) 튜플의 결합2 - 확장
tu1 = 10,20,30
tu2 = 40,50,60
tu1 = tu1 + tu2    #** tu1 += tu2 와 같음
print(tu1)          # (10, 20, 30, 40, 50, 60)
                # => 결합/확장은 가능하지만 튜플 내부의 값은 변하지 않는다 !!!!
# 튜플의 slicing - 리스트처럼 가능
tu3 = tu1[2:]
print(tu3)          # (30, 40, 50, 60)

# packing과 unpacking
# packing : 튜플과 같은 자료형으로 묶어서 사용하는 것
# unpacking : 묶여진 튜플과 같은 자료형을 나눠서 사용하는 것

# 예시) (1,2),(3,4)
# packing => pack = ((1,2),(3,4))
# unpacking => a,b = pack       # a = (1,2) b = (3,4)

a,b,c = 10,20,30    # => 각 변수들 = 튜플 -> unpacking
print(a,b,c)                    # 10 20 30
print(type(a),type(b),type(c))  # <class 'int'> <class 'int'> <class 'int'>

lst = [100,200,300]  
a,b,c = lst         # => 리스트에서도 unpacking이 가능
print(a,b,c)                    # 100 200 300
print(type(a),type(b),type(c))  # <class 'int'> <class 'int'> <class 'int'>

st = 'abc'
a,b,c = st          # => 문자열에서도 unpacking이 가능
print(a,b,c)                    # a b c
print(type(a),type(b),type(c))  # <class 'str'> <class 'str'> <class 'str'>

# print(help('tuple'))
# 튜플의 함수
# index(value) : 튜플에 있는 값에 해당하는 멤버의 인덱스 값을 반환
# count(value) : 튜플에 있는 값의 개수를 반환

# 예제 4
tu = (100,200,'함수',100,'개수')
# idx  0   1    2     3    4
print(tu.index(200))    # 1
print(tu.index(100))    # 0
print(tu.count(100))    # 2

# [문제1]
# numbers = (10,20,30,40,50,60,70)
# 위 튜플 자료에서 30과 40을 따로 num1, num2 변수에 할당하시오
numbers = (10,20,30,40,50,60,70)
num1, num2 = numbers[numbers.index(30)], numbers[numbers.index(40)]
print(num1, num2)

# [문제2]
# menu = (('칼국수',6000),('비빔밥',5500),('돼지국밥',7000))
# 위 자료의 값을 다음처럼 출력하시오
# 칼국수 - 6,000원
# 비빔밥 - 5,500원
# 돼지국밥 - 7,000원
menu = (('칼국수',6000),('비빔밥',5500),('돼지국밥',7000))
for x in menu :
    print("{} - {:,}원".format(x[0],x[1]))
    
# [튜플 종합 문제]
# (문제1)
# 1. 여러 개의 값을 패킹시킨 후 저장되어 있는 값을 빼내어 출력하시오 (5개 값 저장)
# tuple의 값을 리스트에 저장하시오. 단, len 함수를 이용
tu = 10,20,30,40,50
lst = []
for x in tu :
    print(x, end=' ')
print()
for x in range(len(tu)) :
    lst.append(tu[x])
print(lst)    

# (문제2) 아래와 같이 출력시키시오
# --------------------------------------
#    (Tuple)        (List)
#   회사정보    :   삼성전자
#   제품명      :   Galaxy
#   가격정보    :   100원
#   출시일      :   미정
tu = '회사정보','제품명','가격정보','출시일'
lst = ['삼성전자', 'Galaxy', '100원', '미정']
print("-"*25)
print("  (Tuple)\t(List)")
for x in range(len(tu)) :
    print("{:^10}:{:^10}".format(tu[x],lst[x]))
print("-"*25)

# (문제3) 위에서 출력한 내용을 업데이트하시오 (index, insert, remove 전부 사용)
# 가격 : 100 -> 110
# 출시일 : 미정 -> 이번달 말
tu = '회사정보','제품명','가격정보','출시일'
lst = ['삼성전자', 'Galaxy', '100원', '미정']

modif = lst.index('100원')
lst.remove('100원')
lst.insert(modif, '110원')

modif = lst.index('미정')
lst.remove('미정')
lst.insert(modif, '이번달 말')

for x in range(len(tu)) :
    print("{:^10}:{:^10}".format(tu[x],lst[x]))