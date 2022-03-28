# lambda 함수
# 익명 함수로, 일시적으로 사용하는 함수를 의미
# 함수가 생성된 곳에서 필요한 경우 사용한 후 버리는 함수

# (형식)
# lambda 인자리스트 : 표현식
# ex) lam = lambda x : x**2
#     print(lam(8)) => 출력결과 : 64
lam = lambda x : x**2
print(lam(8))

# 예제 1) 다음과 같은 함수를 lambda로 표현

# 함수
def swap(a,b) :
    return b,a
a = 100 ; b = 200
print('swap 전 :',a,b)
a,b = swap(a, b)
print('swap 후 :',a,b)

lam3 = lambda x,y : (y,x)
a = 100 ; b = 200
print('swap 전 :',a,b)
a,b = lam3(a,b)
print('swap 후 :',a,b)

# 예제 2)
lam = lambda a: a*10
lam2 = lambda a,b : a+b
noData = lambda : print('인자가 없는 lambda')

# 결과 확인
print(lam(10))
print(lam2(10,20))
noData()
# noData => 출력 : <function __main__.<lambda>()>

# 예제 3)
def str_len(s) :
    return len(s)

string = ['bob','charles','alexander3','teddy']

# 알파벳 순서대로 정렬 => string.sort(key=str_len) -> 문자열의 길이를 기준으로
string.sort(key=str_len)    # key에는 정렬하고자하는 순서를 가리키는 function str_len이 입력됨
print(string)
# => str_len은 한 번만 쓰고 더 이상 사용되지 않기 때문에 lambda로 활용하는 게 더 메모리효율적임

string = ['bob','charles','alexander3','teddy']
string.sort(key=lambda s : len(s))
print(string)


# lambda가 유용하게 사용되는 3가지 대표적 함수
# filter : 특정 조건을 만족하는 요소만 남기고 필터링
# map : 각 원소를 주어진 수식에 따라 변경하여 새로운 리스트 반환
# reduce : 차례대로 앞 2개의 원소를 가지고 연산. 연산 결과가 그 다음 연산의 입력으로 진행됨
#           => 마지막까지 진행되며, 최종 출력은 한 개의 값만 남김

# filter(함수, 리스트) : 특정 조건을 만족하는 요소만 남기고 필터링
# filter(function, iterable) -> 특정 조건의 요소만 남기고 필터링
#                               리스트에 있는 내용을 함수에 대입하여 결과값을 처리(True or False)

# filter함수를 사용하여 리스트의 짝수만 반환하는 함수 만들기

# (1) 함수를 사용
def even(n) :           # 값이 짝수인지 홀수인지 판단하는 함수
    return n%2 == 0     # n%2 = 0일 때 반환
print(even(3))      # 홀수니까 False 반환

nums = list(range(1,11))    # 1부터 10까지의 수 세팅
filter_list = list(filter(even, nums))
print('함수 사용 :',filter_list)
# -> 하지만 even함수는 한 번만 사용됨 !! => 이럴 때 lambda로 임시함수를 만들어 사용하기

# (2) lambda를 사용
nums = list(range(1,11))
filter2_list = list(filter(lambda n : n%2 == 0, nums))
print('lambda 사용 :',filter2_list)

# map(function, iterable) : 특정 조건에 맞는 새로운 리스트 반환
#                         : 각 멤버를 func으로 동작시킨 후에 새롭게 리스트 생성 => list(map(func, iter1))
# 주어진 리스트의 각 값을 제곱한 새로운 리스트 만들기
nums = list(range(1,10))
print(list(map(lambda n : n**2,nums)))

# reduce : 차례대로 앞 2개의 원소를 가지고 연산. 연산 결과가 그 다음 연산의 입력으로 진행됨
# reduce 함수는 functools 모듈 내에 존재함 (내장함수는 아님)
import functools
a = [1,2,3,5,8]
# 리스트 내의 모든 숫자의 합 구하기
print(functools.reduce(lambda x,y : x+y, a))
print(functools.reduce(lambda x,y : x*y, a))
# reduce (앞 2개의 원소 연산처리하는 lambda 함수, 값들이있는변수)

# [람다 문제] 람다 함수를 사용하여 두 수의 사칙연산하는 프로그램을 작성

lam1 = lambda x,y:x+y
lam2 = lambda x,y:x-y
lam3 = lambda x,y:x*y
lam4 = lambda x,y:x/y
import os
def play() :
    os.system('cls')
    print('사칙연산 시작!')
    x = int(input('연산할 첫번째 수를 입력하세요 : '))
    giho = input('연산 기호를 입력하세요 : ')
    y = int(input('연산할 두번째 수를 입력하세요 : '))
    print('연산 결과 : ',end='')
    
    if giho == '+' : print(lam1(x,y))
    elif giho == '-' : print(lam2(x,y))
    elif giho == '*' : print(lam3(x,y))
    elif giho == '/' : print("{:.2f}".format(lam4(x,y)))
while True :    
    play()
    if input('계속하시겠습니까?(y/n) : ') == 'n' : break
    