# python의 문자열 : 파이썬을 사용하는 문자열 처리

# 특징
# 1) 인덱싱을 이용한 참조가 가능
string = 'python string'
print(string[0])    # p
print(string[7])    # s
print(string[-1])    # g

# 2) 슬라이싱을 이용한 참조
print(string[:6])   # python
print(string[0::2]) # pto tig

# 3) 문자열 반복문 (for)
st = 'python string for'
for x in st :
    print(x,end=' ')    # p y t h o n   s t r i n g   f o r 
    
# 문자열 함수
# find(str) : 문자열에서 특정 문자열을 찾아서 해당 문자의 index값을 반환
# count(str) : 문자열에서 특정 문자열을 찾아서 해당 문자열의 수를 반환
# lower() : 문자열에서 영문 대문자를 소문자로 변경하여 반환
# upper() : 문자열에서 영문 소문자를 대문자로 변경하여 반환
# strip() : 문자열에서 양쪽 공백 또는 문자를 제거하여 반환
# lstrip() : 문자열에서 왼쪽 공백 또는 문자를 제거하여 반환
# rstrip() : 문자열에서 오른쪽 공백 또는 문자를 제거하여 반환
# replace(old,new) : 문자열에서 왼쪽(old) 문자열을 찾아서 오른쪽(new) 문자열로 변경
# split() : 문자열을 특정 문자 기준으로 분리 -> 리스트로 반환
print(help('str'))


# find 예제
st = 'python string'
    # 0123456789...
print(st.find('python'))    # 0
print(st.find('string'))    # 7 해당 문자열이 시작하는 인덱스를 찾아줌

# find(str,시작인덱스,끝인덱스)
print(st.find('t'))         # 2
print(st.find('t',3))       # 8 => 중복된 문자열의 인덱스를 찾고자 할 때 시작인덱스를 적용

# find()가 문자열을 찾지 못한 경우의 반환값 : -1 >> 에러가 아님!
print(st.find('t',9))       # -1


# count 예제
st = 'python string'
print(st.count('t'))        # 2
# count(str,시작인덱스,끝인덱스)
print(st.count('t',6))      # 1 => 인덱스 6(공백)부터 찾기


# lower()
st = 'PYTHON STRING'
print(st.lower())   # 반환값으로 변경된 내용을 전달하나, 원래 데이터가 변경되지는 않는다
print(st)           # PYTHON STRING
st1 = st.lower()
print(st1)          # python string

# upper()
st = 'python string'
print(st.upper())
print(st)           # python string
st2 = st.upper()
print(st2)          # PYTHON STRING


# strip() : 양쪽에 인자로 전달 받은 문자열을 제거, 인자값이 없는 경우 공백 제거
st = '     python string     '
print(f"[{st}]")
st1 = st.strip()
print(f"[{st1}]")   # 양쪽 공백 제거됨!

# lstrip()
st2 = st.lstrip()
print(f"[{st2}]")   # [python string     ]

# rstrip()
st3 = st.rstrip()
print(f"[{st3}]")   # [     python string]


# replace(old, new)
st = 'python string'
st1 = st.replace('string', '문자열')
print(st1)      # python 문자열


# split(str) : 문자열을 str에 있는 문자 기준으로 분리 -> list로 저장
st = 'python string'
st1 = st.split()    # 공백을 기준으로 분리
print(st1)          # ['python', 'string']


# split()을 이용한 입력문자 값 분리
values = input("입력 : ").split()   # 입력 : I am a student
print(values, type(values))        # ['I', 'am', 'a', 'student'] <class 'list'>


# 예제 1 - 결합 및 연산
A = 'Have a'
B = ' Nice Day! '
C = A + B           # 'Have a' + ' Nice Day! '
print(C)            # Have a Nice Day!
print(C*3)          # 반복
A += ' Nice Day!!!' # 확장
print(A)            # Have a Nice Day!!!


# [문제1] 
# 문장 변경하기
st = 'NevEr-eVer 100gIVe Up'    # => Never-Ever 100Give Up
st1 = st1.title()
print(st1)
# Have a nice day 문자열에서 'a','day','dak'의 개수 알아오기
st = 'Have a nice day'
print("a의 개수 : {} / day의 개수 : {} / dak의 개수 : {}".format(st.count('a'),st.count('day'),st.count('dak')))
            # a의 개수 : 3 / day의 개수 : 1 / dak의 개수 : 0
    
            
# [문제2] "It is a fun python class" 문자열의 길이, 문자 'a'의 개수, 's'의 개수를 출력하는 코딩 (함수 쓰지 않기)
st = "It is a fun python class"
cnt = cntA = cntS = 0
for x in st :
    cnt += 1
    if x == 'a' : cntA += 1
    if x == 's' : cntS += 1
print("문자열 길이 :",cnt)                                  # 문자열 길이 : 24
print("a의 개수 : {} / s의 개수 : {}".format(cntA,cntS))    # a의 개수 : 2 / s의 개수 : 3


# [문제3] "Have a nice day" 문자열을 가지고 다음을 처리하세요
# 1) 각각 find와 index를 사용하여 "day" 문자의 위치를 찾으세요
# 2) 각각 find와 index를 사용하여 "kkk" 문자의 위치를 찾으세요
# 3) find를 사용하여 첫 번째, 두 번째, 세 번째, 네 번째 'a'의 위치를 출력하세요
st = "Have a nice day"

print("find(day) :",st.find('day'))
print("index(day) :",st.index('day'))

print("find(kkk) :",st.find('kkk'))
#print("index(kkk) :",st.index('kkk')) >> 에러

count = 0
for x in range(st.count('a')) :
    num = st.find('a',count)
    print(f"'a'의 위치 {x+1} : {num}")
    count = num+1
print(f"'a'의 위치 {x+2} : {st.find('a',count)}")

# 선생님 답
idx = st.find('a')
print("첫번째 a의 위치 :",idx)      
idx = st.find('a',idx+1)        # 첫번째 a의 위치 : 1
print("두번째 a의 위치 :",idx)
idx = st.find('a',idx+1)        # 두번째 a의 위치 : 5
print("세번째 a의 위치 :",idx)
idx = st.find('a',idx+1)        # 세번째 a의 위치 : 13
print("네번째 a의 위치 :",idx)
idx = st.find('a',idx+1)        # 네번째 a의 위치 : -1


# [Quiz] : List를 정의하여 색인 위치 저장
# a의 총 개수와 첨자의 위치를 출력하시오
# st = "Have a Nice Day Have a Nice Day Have a Nice Day"
# 결과는 a 개수 : 9 / 첨자 : [1,5,13,17,21,29,33,37,45] 로 출력
st = "Have a Nice Day Have a Nice Day Have a Nice Day"
pcs = cnt = 0
cntA = []
for x in st :
    num = st.find('a',cnt)
    if num != -1 :
        pcs += 1
        cntA.append(num)
        cnt = num+1
print("a 개수 :",pcs)
print("첨자 :",cntA)

# 선생님 답
idx = 0
lst = []
while True :
    idx = st.find('a',idx)
    if idx != -1 : 
        lst.append(idx)
        idx += 1
    else : break
print("a 개수 :",st.count('a'))     # a 개수 : 9
print("첨자 :",lst)                 # 첨자 : [1, 5, 13, 17, 21, 29, 33, 37, 45]


# strip() : 양쪽에 있는 공백 또는 문자를 제거
st = "파이썬파"
print(st)
print(st.strip("파"))   # 이썬
print(st.lstrip("파"))  # 이썬파
print(st.rstrip("파"))  # 파이썬

st = "--1-파이썬-1--"
print(st)
print(st.strip("-"))    # 1-파이썬-1
print(st.lstrip("-"))   # 1-파이썬-1--
print(st.rstrip("-"))   # --1-파이썬-1


# replace() 함수 사용
st = "2015-06-05"
#     0123456789 - index
print(st)
print(st.replace('2015', '2022'))   # 2022-06-05
print(st[:4])                       # 2015 => 원본 데이터는 변하지 않음             
print(st.replace(st[:4], '2022'))   # 2022-06-05


# split(str) : 특정 문자(str)를 기준으로 문자열을 나누는 함수 -> 리스트로 변환
st = "Never Ever Give Up"
a = st.split()
print(st)
print(a,type(a))        # ['Never', 'Ever', 'Give', 'Up'] <class 'list'>

st = "하나:둘:셋"
st1 = "1,2,3"
b = st.split(':')
c = st1.split(',')
print(b,type(b))        # ['하나', '둘', '셋'] <class 'list'>
print(c,type(c))        # ['1', '2', '3'] <class 'list'>

st = "하나둘셋넷"
d = st.split()          # 공백이 없기 때문에 문자열 전체가 한 요소로 그대로 리스트에 저장됨
print(d,type(d))        # ['하나둘셋넷'] <class 'list'>

# splitlines() : 개별 행('\n')을 기준으로 문자열을 나누는 함수 -> 리스트로 저장
st = "Never\nEver\nGive\nUp"
print(st)
print(st.splitlines())  # ['Never', 'Ever', 'Give', 'Up'] - 개행이 각각 요소로 리스트에 저장됨

# 여러줄 문자열 처리 : '''~''' / """~"""        => 엔터와 엔터 사이의 공백까지 문자열로 인식함
st = """Never Ever Give Up
    Never Ever Give Up
Never Ever Give Up
Never Ever Give Up
Never Ever Give Up"""
print(st)
print(st.splitlines())
    # ['Never Ever Give Up', '    Never Ever Give Up', 'Never Ever Give Up', 'Never Ever Give Up', 'Never Ever Give Up']
    
    
# join() : 지정한 문자열을 기준으로 문자열 데이터를 결합 - 반환값은 str
st = '123'
print(st.join('%%'))    # %123%
print('%'.join(st))     # 1%2%3

# 아래의 리스트를 문자열로 변경 -> "I am a student"
lst = ['I', 'am', 'a', 'student']
print(' '.join(lst))                    # I am a student

lst = ["","123","456"]
print("".join(lst))                         # 123456
print("-".join(lst),type("-".join(lst)))    # -123-456 <class 'str'>

lst = ['2015','06','05']
st = "-".join(lst)
print(st)           # 2015-06-05         



# [문자열 실습 1]
# input() 함수로 이름과 나이값을 입력받을 때 한 번에 입력받아 처리하고 출력하는 코드 작성
# 예) 이름과 나이를 입력하세요 : 홍길동 18 => 이름 : 홍길동, 나이 : 18
info = input('이름과 나이를 입력하세요 : ')
lst = info.split()
print(f"이름 : {lst[0]} , 나이 : {lst[1]}")

# 선생님 답 !!!!!!!!!!!
info = input('이름과 나이를 입력하세요 : ')
name, age = info.split()
print(f"이름 : {name} , 나이 : {age}")



# [문자열 실습 2]
# input() 함수로 입력 받은 수의 더하기, 빼기, 곱하기, 나누기의 간단한 수식을 처리할 수 있도록 코드 작성
# 예) 계산식을 입력하세요 : 5+5 / 계산 결과 : 10
exp = input('계산식을 입력하세요(ex.5+5) : ')
if exp.find('+') != -1 :
    lst = exp.split('+')
    result = 0
    for x in lst : result += int(x)
    
elif exp.find('-') != -1 : 
    lst = expa.split('-')
    result = int(lst[0])
    for x in lst[1:] : result -= int(x)
        
elif exp.find('*') != -1 :
    lst = exp.split('*')
    result = 1
    for x in lst : result *= int(x)
    
elif exp.find('/') != -1 :
    lst = exp.split('/')
    result = int(lst[0])
    for x in lst[1:] : result /= int(x)
    
print(result)

# 선생님 답
import os

while True :
    os.system('cls')
    calc = input('계산식을 입력하세요(ex.5+5) : ')
    if '+' in calc :
        num1, num2 = calc.split('+')
        print("계산 결과 :",int(num1) + int(num2))
    elif '-' in calc :
        num1, num2 = calc.split('-')
        print("계산 결과 :",int(num1) - int(num2))
    elif '*' in calc :
        num1, num2 = calc.split('*')
        print("계산 결과 :",int(num1) * int(num2))
    elif '/' in calc :
        num1, num2 = calc.split('/')
        print("계산 결과 : {:.2f}".format(int(num1) / int(num2)))
    else : print("수식 입력이 잘못되었습니다")
    if int(input("계속하시겠습니까 ? (계속 : 1 / 종료 : 0) : ")) == 0 : break
print("계산기 프로그램 종료!")
               

