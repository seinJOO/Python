# 함수(Fuction) : 프로그램에서 사용할 기능을 미리 정의해서 구현하는 것
#                 또다른 의미의 프로그램 내의 프로그램 (큰 범위의 기능)

# python의 함수 정의(생성)
# def 함수이름([인자list]) :
#     함수 기능에 대한 정의1
#     함수 기능에 대한 정의2
#     함수 기능에 대한 정의3
# 
# 1) 함수 사용에 있어 설명이 필요한 경우, 함수 내부에 여러줄 주석을 사용하여 기술
# 2) 함수를 만들 때 함수의 기능을 바로 알 수 있는 이름으로 정의하기(권장)
# 3) 미리 만들어 놓은 함수를 호출 시에는 "함수이름([인자...])"로 호출
# 4) 정의하여 생성된 함수의 반환값이 있는 경우 "return" 명령어를 사용함
#       -> 함수에 반환값이 있는 경우 "return"을 사용, 없는 경우에는 "return"으로 함수 종료
# 5) 필요 시 함수에 인자값을 전달할 수 있음. 전달된 인자값(value)은 함수 정의시에 만든 "매개변수"에 그 값이 저장됨
#       -> 이후 함수 정의부에서 해당 내용을 가지고 구동된다


# [예제1] 사용자가 입력한 값을 출력하는 함수 구현

# 함수의 정의
def pr() :  #인자값 없이 처리되는 함수
    txt = input("입력값 : ")
    print()
    print("입력한 내용은 :",txt)
# 함수 호출
pr()

# [실습1] 입력값을 받아서 사칙연산하는 프로그램 함수를 사용 - calc()로 구현
import os
def calc() :
    while True :
        os.system('cls')
        exp = input('식을 입력해주세요 : ')
        if '+' in exp :
            num1, num2 = exp.split('+')
            print("계산 결과 :",int(num1)+int(num2))
        elif '-' in exp :
            num1, num2 = exp.split('-')
            print("계산 결과 :",int(num1)-int(num2))
        elif '*' in exp :
            num1, num2 = exp.split('*')
            print("계산 결과 :",int(num1)*int(num2))
        elif '/' in exp :
            num1, num2 = exp.split('/')
            print("계산 결과 :","{:.2f}".format(int(num1)/int(num2)))
        else :
            print('수식이 잘못 입력되었습니다.')
        chk = input('사칙연산을 계속하시겠습니까?(y/n) : ')
        if chk == 'n' : break    

calc()

# [예제 2] 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수 구현
#                           사용자로부터 입력받은 값을 인자값으로 처리하는 함수

# 함수 정의
def pr2(str1) :
    print("입력한 내용은 : ",str1)
# 메인
txt = input("입력 : ")
print()
print(txt)

# [실습 2] 실습1의 입력값을 인자값으로 사용하여 함수 구현

import os
def calc(exp) :
    os.system('cls')
    if '+' in exp :
        num1, num2 = exp.split('+')
        print("계산 결과 :",int(num1)+int(num2))
    elif '-' in exp :
        num1, num2 = exp.split('-')
        print("계산 결과 :",int(num1)-int(num2))
    elif '*' in exp :
        num1, num2 = exp.split('*')
        print("계산 결과 :",int(num1)*int(num2))
    elif '/' in exp :
        num1, num2 = exp.split('/')
        print("계산 결과 :","{:.2f}".format(int(num1)/int(num2)))
    else : print('수식이 잘못 입력되었습니다.')
         
while True :
    os.system('cls')
    exp = input('수식을 입력해주세요 : ')
    calc(exp)    
    if input('사칙연산을 계속하시겠습니까?(y/n) : ') == 'n' : break

# [예제 3] 사용자로부터 입력받은 값을 return을 사용하여 반환하는 함수
# 함수 정의
def pr3(str1) :
    return "입력한 문자열 : " + str1
# 메인
txt = input("입력 : ")
print(pr3(txt))

# [실습 3] 위 내용을 토대로 계산 결과를 반환값으로 처리하는 함수로 변환

import os
def calc(exp) :
    result = 0
    if '+' in exp :
        num1, num2 = exp.split('+')
        return int(num1)+int(num2)
    elif '-' in exp :
        num1, num2 = exp.split('-')
        return int(num1)-int(num2)
    elif '*' in exp :
        num1, num2 = exp.split('*')
        return int(num1)*int(num2)
    elif '/' in exp :
        num1, num2 = exp.split('/')
        return "{:.2f}".format(int(num1)/int(num2))
    else : return "Error"
         
while True :
    os.system('cls')
    exp = input('수식을 입력해주세요 : ')
    print("수식 결과 : ",calc(exp))
    if input('사칙연산을 계속하시겠습니까?(y/n) : ') == 'n' : 
        print('사칙연산 종료 !')
        break
    
# [실습 4] 두 수에 대한 한 번의 계산식을 입력받아서 결과를 출력
# 사용자가 계산식을 입력, 이것을 이용하여 처리
# calc()가 인자값으로 두 정수와 연산기호를 인자로 받아 처리하는 함수 만들기

# 함수 정의
def calc(num1,cal,num2) :
    result = 0
    if cal == '+' :
        return num1 + num2
    elif cal == '-' :
        return num1 - num2
    elif cal == '*' :
        return num1 * num2
    elif cal == '/' :
        return "{:.2f}".format(num1 / num2)
    else : return "Error"
# 메인    
import os
while True :
    os.system('cls')
    num1 = int(input('숫자를 입력해주세요 : '))
    cal = input('연산 기호를 입력해주세요 : ')
    num2 = int(input('숫자를 입력해주세요 : '))
    print("수식 결과 : ",calc(num1,cal,num2))
    if input('사칙연산을 계속하시겠습니까?(y/n) : ') == 'n' : 
        print('사칙연산 종료 !')
        break
    
# 함수 인자 기본값(default) 설정
# default : 입력 인자값이 없는 경우에 기본적으로 적용되어지는 값

# 형식)
# def 함수이름(param1, param2=1) :
#   함수정의문1
#   함수정의문2

# 이렇게 정의된 함수가 있는 경우, param2는 기본값으로 1을 가지고 있다
# => 즉, 인자값으로 param2에 전달되지 않아도 기본값으로 1을 가진다

# [예제 4] 함수 인자의 기본값 설정(인자1)
def pr4(par1 = 10) :
    print(par1)
# 메인
pr4()       # 값을 넣지 않으면 기본값으로 구동됨
pr4(20)     # 값을 넣으면 넣은 값으로 구동됨

# 인자를 2개 가진 경우 (모두 default인 경우)
def pr5(par1=10, par2=20) :
    print(par1,par2)
# 메인
pr5()           # 10 20
pr5(15)         # 15 20
pr5(par2=100)   # 10 100
pr5(100,200)    # 100 200

# 인자가 2개 이상, 기본값 1인 경우
def pr6(par1, par2=20) :
    print(par1,par2)
pr6(100,200)    # 100 200
pr6(100)        # 100 20
pr6(200)        # 200 20
# pr6() -> TypeError : pr6() missing 1 required positional argument: 'par1'

# 인자의 기본값이 맨 앞에 있는 경우 => 기본값 뒤에는 일반 인자가 존재할 수 없다 !!!!!!
#def pr7(par1=10, par2) :    => SyntaxError : non-default argument follows default argument
def pr7(par1, par2=10) :
    print(par1,par2)
pr7()

# [예제 4] 거꾸로 수를 반환하는 함수를 계산, 출력 기능으로 나눠서 작성 (123=>321)
def rev(nums) :
    '''거꾸로 수 반환'''
    result = 0; cnt=-1; tmp = nums
    while tmp > 0 :        
        tmp = tmp//10
        cnt += 1
    for x in range(cnt,-1,-1) :
        step = abs(x-cnt)
        result += (nums // 10**x) * 10**step
        nums = nums % 10**x
    print("찐:",result)
    
rev(5842684)

# [Quiz]
# 1) 짝,홀수를 구분하는 함수 작성
def odd(num) :
    if num % 2 == 0 : 
        return "짝수"
    else : 
        return "홀수"
num = int(input('숫자를 입력하세요 : '))
print(odd(num))

# 2) 3의 배수를 판별하는 함수 작성

def triple(num) :
    if num % 3 == 0 : 
        return "3의 배수입니다"
    else : return "3의 배수가 아닙니다"

num = int(input('숫자를 입력하세요 : '))
print(triple(num))

# 3) 계산기를 입력,출력,연산기능으로 나눠서 실행하도록 작성(입력->계산처리->출력)
# 함수 정의
def into() :
    num1 = int(input('숫자를 입력해주세요 : '))
    cal = input('연산 기호를 입력해주세요 : ')
    num2 = int(input('숫자를 입력해주세요 : '))
    return num1, cal, num2
    
def calc(num1,cal,num2) :
    result = 0
    if cal == '+' :
        return num1 + num2
    elif cal == '-' :
        return num1 - num2
    elif cal == '*' :
        return num1 * num2
    elif cal == '/' :
        return "{:.2f}".format(num1 / num2)
    else : return "Error"
    
def output(into) :
    num1, cal, num2 = into
    result = calc(num1, cal, num2)
    print(num1,cal,num2,"=",result)
    
# 메인    
import os
while True :
    os.system('cls')
    output(into())
    if input('사칙연산을 계속하시겠습니까?(y/n) : ') == 'n' : 
        print('사칙연산 종료 !')
        break
    

# 4) 거꾸로 수를 반환하는 함수를 계산, 출력 기능으로 나눠서 작성(123->321)        
def rev(nums) : 
    '''거꾸로 수 반환'''
    result = 0
    while nums > 0 :         
        result = result*10 + (nums % 10)
        nums = nums // 10
    return result

def prt(result) :
    print("입력한 숫자를 거꾸로 하면 :",result) 

import os
while True :
    os.system('cls')
    nums = int(input('숫자를 입력하세요 : '))
    result = rev(nums)
    prt(result)
    if input('계속하시겠습니까?(y/n) : ') == 'n' : 
        print('종료 !')
        break

       
# [예제 5] 친구 이름 관리를 함수로 기능을 나눠서 작성하세요
# 1. 친구목록보기, 2. 친구추가, 3.친구삭제, 4.친구수정, 0.종료
# 이름 성별 나이
def select() :
    print('1. 친구목록보기, 2. 친구추가, 3.친구삭제, 4.친구수정, 0.종료')
    sel = input('메뉴를 선택하세요 >> ')
    if sel not in [0,1,2,3,4] :
        sel = int(input('입력 오류! 메뉴를 선택하세요 >> '))
    return sel
    
def view(friends) :
    for x in friends :
        print("{}) 이름 : {} 성별 : {} 나이 : {}".format(friends.index(x)+1,x[0],x[1],x[2]))
    print()

def add(friends) :
    name = input('친구의 이름을 입력하세요 : ')
    gender = input('친구의 성별을 입력하세요(남/여) : ')
    age = int(input('친구의 나이를 입력하세요(숫자만) : '))
    new = [name,gender,age]
    friends.append(new)
    print()
    return friends

def remove(friends) :
    view(friends)
    idx = int(input('삭제할 친구의 번호를 입력하세요 : '))
    friends.pop(idx-1)
    print()
    return friends

def modify(friends) :
    view(friends)
    idx = int(input('변경할 친구의 번호를 입력하세요 : '))
    target = input('무엇을 변경하시겠습니까? : ')
    new = input('변경할 내용을 입력하세요 : ')
    for x in friends :
        if friends.index(x) == idx-1 :
            if target == '이름' :
                x[0] = new
            elif target == '성별' :
                x[1] = new
            elif target == '나이' :
                x[2] = int(new)
    print()
    return friends

def end() :
    print('프로그램 종료')

import os
friends = []
while True :
    os.system('cls')
    sel = int(select())
    if sel == 1 :
        view(friends)
        os.system('pause')
    elif sel == 2 :
        friends = add(friends)
    elif sel == 3 :
        friends = remove(friends)
    elif sel == 4 :
        friends = modify(friends)
    elif sel == 0 :
        end(); break
    
# [문제] 알바 시급 프로그램 작성 (default 인자값 사용)
# 시급 : 8500원, 하루 8시간, 한달 30일(기본값)
# 다음과 같이 출력하세요
# <<시급 계산 프로그램>>
# 1. 기본급
# 2. 일한 날짜 입력
# 번호 입력 >>

def defWage(days=30, wage=8500, time=8) :
    print("이번 달의 총 급여는 {:,}원 입니다.".format(days*wage*time))

def sel() :
    print('<<< 시급 계산 프로그램 >>>')
    print('1. 기본급 \n2. 일한 날짜 입력')
    sel = int(input('번호 입력 >>'))
    return sel

def getDays() :
    days = int(input('이번 달에 일한 기간을 입력해주세요 : '))
    return days

sel = sel()
if sel == 1 :
    defWage()
elif sel == 2 :
    defWage(getDays())
    
    
# 인자값 처리 방식 1 => 연속된 자료를 처리하는 함수의 인자 처리 방식

# 예제
def pr8(a,b,c) :
    print(a,b,c)
    
pr8(10,20,30)   # 10 20 30

# "*"를 이용하여 리스트 또는 튜플과 같은 자료를 연속된 인자값으로 처리
# 리스트 또는 튜플의 변수값을 받아서 "unpacking"
x = [100,200,300]
y = [10,20]
z = 1,2,3,4

# pr8(x)    => TypeError: pr8() missing 2 required positional arguments: 'b' and 'c' 
#                       인자값이 함수가 필요로 하는 개수보다 적음(리스트로 입력되기 때문)
pr8(*x)     # 100 200 300 리스트 형태가 아님!! 각각의 요소들이 각각 출력됨
pr8(*y,30)  # 10 20 30
# pr8(*z)   => TypeError: pr8() takes 3 positional arguments but 4 were given 
#                       인자값이 함수가 필요로 하는 개수보다 많음