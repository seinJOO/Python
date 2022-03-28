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