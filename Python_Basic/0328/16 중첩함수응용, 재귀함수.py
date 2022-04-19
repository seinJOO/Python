### 획득자(getter), 지정자(setter), nonlocal
# 내부 함수는 중첩함수에서 함수 클로저 역할도 하지만,
# 함수 내의 자료를 외부로부터 획득(획득자:getter)하거나 자료를 수정하는 역할(지정자:setter)도 한다 !

# 획득자 함수 : 함수 내부에 생성한 자료를 외부로 반환하는 함수. 반드시 return 명령어를 가진다
# 지정자 함수 : 함수 내부에 생성한 자료를 외부에서 수정하는 함수. 반드시 매개변수를 가진다
#             만약 외부함수에서 생성된 자료를 수정할 경우 해당 변수에 nonlocal 명령어를 쓴다

# (형식)
# def 외부함수() :
#   변수명 = 값1
#   def 내부함수() :
#       nonlocal 변수명
#       변수명 = 값2

# 예시) 획득자와 지정자 함수, nonlocal 명령어를 이용하여 외부함수에서 생성한 자료를 외부에서 획득하고 수정하기
def main_func(num) :
    num_val = num       # 자료 생성
    def getter() :      # 획득자 함수 - return값 필수
        return num_val
    def setter(value) : # 지정자 함수는 반드시 인자값(매개변수)을 가짐
        nonlocal num_val
        num_val = value
    return getter, setter   # 함수 클로저 반환

# 함수 호출
getter, setter = main_func(100)     # num_val 생성

# 획득자 getter 호출
print('num =',getter())     # 획득한 num_val 확인

# 지정자 setter 호출
setter(200)     # num_val 값 수정
print('num =',getter())     # 수정한 num_val 값 확인


### 함수 장식자(decoration) : 기존 함수 시작부분과 종료부분에 기능을 장식하여 추가해주는 별도의 함수
# 현재 실행되는 함수를 파라미터로 받아서 꾸며줄 내용과 함께 해당 함수를 감싸주는 함수(Wrapping function)

# (형식)
#   @함수 장식자    => 함수장식자는 사전에 만들어져 있어야 함! @wrapping함수명(어노테이션처럼 씀)
#   def 함수명() :
#       함수 실행문

# wrapper함수 정의
def wrap(func) :    # 함수를 파라미터로 받는다
    def decorated() :
        print('반가워요~!')   # 함수의 시작부분에 삽입
        func()              # 인수로 넘어온 주 함수를 실행시킴
        print('잘가요~~!')    # 함수의 종료부분에 삽입
    return decorated        # 클로저 함수 반환

# 장식자를 적용할 실제 함수 정의
@wrap
def hello() :
    print('저는 세니입니당')

# 함수 호출하여 실행하기
hello()

# 재귀함수(Recursive Function)
# 함수 내부에서 자신의 함수를 반복적으로 호출하는 함수

# 특징(중요)
# 재귀함수는 반복적으로 호출하기 때문에 반드시 함수 내에 반복을 탈출(exit) 조건이 필수
# 재귀함수는 반복적으로 변수를 조금씩 변경하여 연산을 수행하는 알고리즘에서 이용됨
# 예제로 팩토리얼(Factorial) 계산 등이 있음

# stack과 비슷한 구조! 가장 먼저 실행된 함수가 가장 나중에 종료된다 => cal1 -> cal2 -> cal3 -> cal4 - (탈출구문 실행) -> cal4 -> cal3 -> cal2 -> cal1
# 탈출코드가 있어야 무한히 반복되지 않고 빠져나올 수 있음

# 예제) 카운트 - 1부터 n까지 정수의 개수를 count()하는 과정

# 재귀함수 정의
def Counter(n) :
    if n == 0 : 
        print()
        return 0    # 종료조건
    else :
        print(n, end=' ')
        Counter(n-1)    # 재귀함수 호출

# 함수 호출 1
print('n = 0 :',Counter(0))     # n = 0, 0

# 함수 호출 2
print(Counter(5))    

# 예제) 누적합 - 1부터 n까지 정수를 카운트한 값을 누적하여 반환하는 경우

# 재귀함수 정의
def Adder(n) :
    if n == 1 :     # 종료 조건 (누적값이기 때문에 0은 관련 없음)
        return 1
    else :
        result = n + Adder(n-1)     # 재귀호출 : n=1이어서 종료되는 시점에서 탈출 시작
        print(n,end=' ')            # => 스택 영역에서 2 3 4 5 순서로 실행됨
        return result

# 함수 호출 1
print('n = 1 :',Adder(1))
print('n = 5 :',Adder(5))
        
