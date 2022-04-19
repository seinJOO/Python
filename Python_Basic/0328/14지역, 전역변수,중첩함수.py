# 변수의 범위

# 지역변수 - 특정 지역에서만 사용되는 지역변수 (블럭 내 사용)
# 전역변수 - 지역에 상관없이 전 영역에서 사용되는 전역변수
# 특정 영역(블럭)은 함수 또는 블럭(if, for, while 등)등을 의미함
# 전역변수 - global, 지역변수 - local
# 전역변수는 지역변수보다 메모리 소모가 크다 ! 항상 저장되어 있어야 하기 때문에
# 다만, 요즘은 큰 차이는 없긴 하다 . . .

# 예제1 - 전역변수의 영역 : 블럭에서만 동작
var2 = 2
def func(arg) :
    var1 = 1
    print(var1, arg)

func(var2) # => global변수이기 때문에 함수의 인자값으로 대입 가능
# print(var1) -> NameError : name 'var1' is not defined 
#               => 선언된 장소인 함수 func의 블럭 내에서만 사용 가능 - 함수가 종료되면서 사라짐


# 예제2 - 블럭에서 전역변수를 사용
# global 변수, 전역변수
var2 = 2
print("전역변수 저장위치 :",id(var2))
def func(arg) :
    #var2 = 1       # => 전역변수를 가져온 게 아닌, 새로 생성된 지역변수임
    global var2     # => 전역변수 호출
    print("전역변수 저장위치 :",id(var2))
    var2 = 10
    print(var2, arg+2)
    
func(var2)
print(var2)


# 함수 또는 블럭에서 변수명으로 데이터에 접근 시 우선순위 : 가까운 local > global
# 예제 3

var2 = 2
print("전역변수 저장위치 :",id(var2))
def func(arg) :     # arg값으로 var2 = 2가 들어옴
    global var2         # => 전역변수 var2 호출
    var2 = 10           # => 전역변수 var2 = 10
    var1 = 1
    print(var2, arg+2)      # var2 = 10, 4
    def func2(var2) :
        var2 = 1
        print(var2, arg, var1)    # var2 = 1, 
                                  # arg(var2) = 2 
                                  # => 정의된 변수가 없으면 가장 가까운 장소에서 같은 이름의 변수값을 가져옴,
                                  # var1 = 1
    func2(var2)
    
func(var2)
print(var2)     # 10 => 함수 내에서 호출된 전역변수의 값이 바뀌었음 !!!

# 중첩함수
# 중첩함수란, 함수 내부에 또 다른 함수가 내장된 형태
# 내부 함수를 포함한 함수를 외부함수라고 함

# (형식)
# def 외부함수(인수) :
#      함수 정의문1
#      def 내부함수(인수) :
#           함수 정의문 1
#           return 값
#      return 내부함수

# 파이썬의 중첩함수는 외부함수나 내부함수를 변수에 저장할 수 있다
# 이런 특성을 가지는 함수를 일급함수(First Class Function)라고 함
# 특히, 내부함수는 외부함수의 return 명령문을 이용하여 반환하는 형태의 함수를 클로저(Function closure)라고 함

# 클로저에서 외부함수와 내부함수의 역할
# 외부함수 : 함수에서 사용할 자료를 만들고, 내부함수를 포함하는 역할
# 내부함수 : 외부 함수에서 만든 자료를 연산하고 조작하는 역할을 담당


# 클로저 closure
# 외부함수가 종료되어도 내부함수에서 선언된 변수가 메모리에서 소멸하지 않은 상태로 내부함수를 사용할 수 있음
def a() :       # outer : 외부함수
    var1 = 1
    print('a 함수 종속문')
    def b() :   # 내부함수
        print('b 함수 종속문')
        print(var1)
    return b    # 함수를 리턴할 때는 함수명을 써야 함수가 그대로 전달됨 !!

b = a()     # a 함수 종속문
# 외부 함수 호출 : a 함수 구동 ->  b함수의 정의만 넘겼을 뿐 b가 실행되지 않음
# print('a 함수 종속문')을 실행하면서 return b = 함수 b의 정의가 변수 b에 저장됨
# a함수는 종료되었지만 b함수에 대한 정의는 전달된 상태

b()         # b 함수 종속문 1
# 내부 함수 호출 : b 함수 구동 -> b에 저장된 함수 b의 정의(함수 저장 위치)를 호출해서 실행함

# [예제] ==================================================================
data = list(range(1,101))       # 1~100까지의 숫자 리스트 생성

# outer function
def outer_func(data) :
    dataSet = data  # data로 받은 값을 dataSet 변수에 대입 (= Shallow Copy)
    
    # inner function
    def tot() :
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val) :
        avg_val = tot_val / len(dataSet)
        return avg_val
    return tot, avg     # inner 반환

# 메인

tot, avg = outer_func(data)     # 외부함수 호출 : data 인자값 넣기
# 외부함수에서 dataSet 변수에 인자값을 대입하고, 각 내부함수의 정의들이 각 변수에 대입됨 = unpacking

# 내부함수 호출
# 외부함수가 호출되어 이미 dataSet에 data를 대입하는 종속문이 실행 후 종료되었음에도 불구하고,
# 내부함수가 동작할 때는 dataSet의 값이 존재하여 내부함수 실행 시 잘 대입됨 !!! => 이게 바로 클로저 ~~~!!!!

tot_val = tot()
print("tot =",tot_val)
# outer_func 내에 있는 tot()함수의 리턴값이 tot_val에 대입됨
avg_val = avg(tot_val)
print("avg =",avg_val)
# outer_func 내에 있는 avg()함수의 리턴값이 avg_val에 대입됨



# [Quiz]
# 디폴트 매개변수를 이용한 요금 구하는 프로그램 만들기
# 기본 요금은 500원 / 환승이 없거나 환승 1회까지는 기본요금 
# 1회를 초과하는 환승의 경우 환승 1회마다 요금의 2배씩 증가
# ex. 환승 2회인 경우 : 1000원 환승 3회인 경우 : 2000원
# 장거리는 10000원으로 처리 (최대 요금이 10000원)
# 1. 환승 안함
# 2. 환승 함 -> 몇번 환승하는지 질의 후 요금 계산
# 3. 장거리
# 함수화하여 작업하세요 !! -> 요금 계산하는 함수, 화면에 표시하는 함수
# 함수 처리 시 목적지에 대한 내용도 입력 받아서 처리 !!

def tariff(trf) :
    fee = trf
    def noTF() :
        return fee
    def yesTF(cnt) :
        nonlocal fee    # 내부함수가 지역변수(fee)의 값을 다시 할당하고자 할 때 nonlocal로 선언
        if cnt > 1 :
            for x in range(cnt-1) :
                fee *= 2
                if fee > 10000 :
                    fee = 10000
                    break
        return fee
    def longDist() :
        fee = 10000
        return fee
    return noTF, yesTF, longDist

def prtFee() :    
    noTF, yesTF, longDist = tariff(500)
    place = input('목적지를 입력하세요 : ')
    select = int(input('메뉴를 선택하세요\n1. 환승안함 \n2. 환승 함 \n3. 장거리 \n'))
    if select == 1 : 
        fee = noTF()
    elif select == 2 : 
        cnt = int(input('환승 횟수를 입력하세요 : '))
        fee = yesTF(cnt)
    elif select == 3 : 
        fee = longDist()
    print("{}까지의 요금은 {:,}원 입니다".format(dest,fee))

while True :
    prtFee()
    if input('계속하시겠습니까?y/n : ') == 'n' : break
    
    
# 선생님 답
def transfer(dest, tf, fee=500) :
    for i in range(1,tf) :
        fee *= 500
        if fee >= 10000 : 
            fee = 10000
            break
    return '{}까지의 요금은 {:,}원 입니다'.format(dest, fee)

def display() :
    dest = ""; tf = 0   # 목적지, 환승횟수 초기화
    num = input('1. 환승안함 \n2. 환승 함 \n3. 장거리 \n')
    dest = input('목적지 입력 : ')
    if num == '1' :
        result = transfer(dest)
    elif num == '2' : 
        tf = int(input('환승 횟수를 입력하세요 : '))
        result = transfer(dest, tf)
    elif num == '3' : 
        result = transfer(dest, 1,10000)
    else : 
        print("메뉴 선택이 잘못되었습니다")
        return
    print(result)    
 
 
### match ~ case 구문 : 파이썬 3.10.0 이후에 도입 (switch ~ case 구문과 같은 동작) ===================

# 예제 1
def num_chk(st) :
    match st :      # 확장팩에 아직 업데이트가 안되어서 IndentationError가 뜸 - 무시하기!
        case 1 : return '일'
        case 2 : return '이'
        case 3 : return '삼'
        case _ : return '선택 범위 밖 숫자'

st1 = int(input(' 1 ~ 3 까지의 숫자를 입력하세요 : '))
print('입력값은 '+num_chk(st1)+'입니다')

# 예제 2
def alpha_chk(chk) :
    match chk :
        case 'a'|'A' : return 'A'
        case 'b'|'B' : return 'B'
        case 'c'|'C' : return 'C'
        case _ : return 'A ~ C 이외의 알파벳'

st2 = input('알파벳 a~c 중 한 개를 입력하세요 : ')
print('입력한 알파벳은 :',alpha_chk(st2))

# 연습 : 국가명을 입력받아서 해당 국가 번호를 출력하는 함수 구현

# 01 UnitedState 33 France 34 Spain 81 Japan 82 Korea

# 인자값/반환값의 자료형을 아래와 같이 지정할 수 있다 (인자값 문자열, 반환값 정수)
def getPhoneCode(nat:str) -> int :
    match nat.lower() :
        case 'unitedstate' : return 1
        case 'france' : return 33
        case 'spain' : return 34
        case 'japan' : return 81
        case 'southkorea' : return 82
        case _ : return -1
nat = input('국가명을 영문으로 입력하세요')
print('{}의 국가 번호는 : {:02}'.format(nat, getPhoneCode(nat)))
        