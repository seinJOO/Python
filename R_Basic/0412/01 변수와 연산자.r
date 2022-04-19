## R 사용 문법

# 변수 사용하기 (대입 연산은 "=" 대신 "<-" or "->")
# 1. 하나의 값을 변수 저장하기
x <- 5
x * x

10 -> y
y + y

# 2. 여러 개의 값을 변수에 저장하기 (배열과 같은 자료 사용하기)
x <- c(5, 6)     # 벡터변수, 여러개의 값을 하나의 변수에 저장
print(x)

# 여러 개의 값을 가진 변수에 일부 값을 참조할 때 인덱스를 사용
# R의 인덱스의 시작값은 1부터 !
x[1]
x[2]

## 변수 이름 규칙
# 변수 이름은 영문, 숫자, ".", "_" 를 사용
# "."은 변수 맨앞에 사용 가능 / ".숫자" 는 불가
# "_"는 변수 맨앞에 사용 불가 / "_숫자" 는 사용 가능
# 변수명은 대소문자 구분
# 예약어 사용 불가

## 데이터 타입
# numeric : 숫자(정수, 실수 모두 포함)
# integer : 정수 (표현 : "숫자L")   => (1L = 1 , 55L = 55, 100L = 100)
# complex : 복소수형(i를 붙여서 구분)
# character : 문자/문자열 자료
# logical : 논리자료 (TRUE/FALSE)                                                       #nolint

## 타입을 조회하는 명령어(함수) : class()
print("class()"); class(10i) ; class("wow") ; class(TRUE)

print("=======")
# 형변환 : as.numeric(), as.integer(), as.complex()
x <- 3L
class(x)
a <- as.numeric(x)
class(a)

y <- 2
class(y)
b <- as.integer(y)
class(b)


## 연산자(산술)
# + , - , * , / , ^(제곱) , %%(나머지) , %/%(몫)
3 %% 2  # 1
3 ^ 2   # 9
5 %/% 2 # 2

## <- , <<- , -> , ->>
# <<- : 전역(변수) 선언 & 대입   ,   <- : 대입 처리

# 일반 변수 설정
txt <- "awesome"
my_func <- function() {
    txt <- "fantastic"  # 전역변수와 다른 주소의 변수
    paste("R is", txt)
}
my_func()       # "R is fantastic"
print(txt)      # "awesome" : 함수 안의 txt는 지역변수임을 알 수 있음!

# 전역변수 설정
my_func2 <- function() {
    txt <<- "fantastic"  # 전역변수와 다른 주소의 변수
    paste("R is", txt)
}
my_func2()  # "R is fantastic"
print(txt)  # "fantastic" : 함수 내에서 전역변수 txt에 값을 대입하여 전역변수 값이 변경됨 !


## 비교 연산자
# == , != , < , > , <= , >=

10 == 10
10 != 10
10 > 10
10 < 10
10 >= 10
10 <= 10

## 논리 연산자
# & , && , | , || , !

10 == 10 && 10 == 11        # FALSE : AND연산자
10 == 10 || 10 == 11        # TRUE : OR연산자
!(10 == 10)                 # FALSE : 결과값의 부정 (Ture -> False 출력 / False -> True 출력) # nolint

## 이외 연산자
# : 순서대로 숫자를 생성하는 연산자 ex) 1:10 -> x   => (1,2,3,4,5,6,7,8,9,10) -> x
# %in% : 데이터들(벡터) 내에 값이 있는지 확인 (파이썬의 멤버연산자 in과 같음)
# %*% : 매트릭(행렬) 곱셈

1:10 -> x
x           # 1  2  3  4  5  6  7  8  9 10
i <- 5
i %in% x    # TRUE : i의 값이 x에 포함됨

# print() : 화면에 출력
# paste() : 동일한 자료형의 여러 데이터를 붙여서 출력해줌 (자료형 주의 !!!!)

print(x)        # 1  2  3  4  5  6  7  8  9 10
paste(x, i)
print(i)        # "1 5"  "2 5"  "3 5"  "4 5"  "5 5"  "6 5"  "7 5"  "8 5"  "9 5"  "10 5" # nolint
paste('I', 'am', 'a', 'student')    # "I am a student"  => 각 개별 값들을 붙여서 사용하고 싶을 때 paste를 씀 !  # nolint
# print('I', 'am', 'a', 'student')    # 에러 : 강제형변환에 의해 생성된 NA 입니다   # nolint

### 내장 함수
# max(), min(), sqrt() : 루트연산, abs() : 절대값
# ceiling() : 올림, floor() : 내림, round() : 반올림

max(c(11, 5, 36, 3, 4, 8, 33))        # 36
min(c(11, 5, 36, 3, 4, 8, 33))        # 3
sqrt(3)             # 1.732051 = 루트3                                                          # nolint
abs(-100)
ceiling(1.4)        # 2
floor(1.4)          # 1
round(1.456, 2)      # 1.46 - 소수점 두자리수까지
