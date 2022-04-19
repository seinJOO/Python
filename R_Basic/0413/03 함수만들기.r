### 함수만들기 (function 명령어 사용)
# 함수명 <- function(인자리스트) {
#       함수 정의
#   }

## 함수 호출 : 함수명(인자)
## return() : 함수 내에서 결과값 리턴

fact <- function(x) {
    res <- 1
    for (i in 2:x) {
        res <- i * res
    }
    return(res)
}
fact(5)

## 중첩 함수 1
nested <- function(x, y) {
    a <- x + y
    return(a)
}
nested(nested(2, 2), nested(2, 3))   # 출력결과 : 9 (2+2)+(2+3)                                     #nolint

outer_func <- function(x) {
    inner_func <- function(y) {
        a <- x + y
        return(a)
    }
    return(inner_func)
}

output <- outer_func(3)     # output에 x가 3인 inner_func이 대입됨
output(5)   # 출력결과 : 8   inner_func의 인자값 y에 5를 대입하여 3 + 5 = 8이 출력됨

# 예제 : 숫자를 입력받아 그 숫자를 역으로 출력하는 프로그램을 함수로 만들기
rev <- function(x) {
    res <- 0
    while (TRUE) {
        tmp <- x %% 10
        res <- res * 10 + tmp
        x <- x %/% 10
        if (x == 0) {
            break
        }
    }
    return(res)
}
a <- readline("숫자를 입력하세요 : ")
a <- as.numeric(a)
rev(a)


# 예제 : 두 수를 입력받아 그 평균을 구하는 함수
avg <- function(x, y) {
    res <- sum(x, y) / 2
    return(res)
}

b1 <- readline("평균 구하기 - 첫번째 수 입력 : ")
b1 <- as.numeric(b1)
b2 <- readline("평균 구하기 - 첫번째 수 입력 : ")
b2 <- as.numeric(b2)
avg(b1, b2)

## 재귀함수 : 재귀함수는 자신이 자신을 참조하여 동작하는 함수

rec <- function(x) {
    if (x > 0) {
        res <- x + rec(x - 1)
        print(res)      # 출력은 1 3 6 10 15 => 재귀함수는 연산(5 4 3 2 1) 후 중단점으로부터 탈출 시(1 2 3 4 5) 결과값을 빼옴       #nolint
    } else {
        res <- 0
        return(res)     # x가 0일 때 결과값으로 0을 리턴 -> rec(0)이 되어 함수 중단
    }
    return(res)
}
rec(5)

# 재귀함수를 사용하여 팩토리얼 계산 함수 생성

fact_r <- function(f) {
    if (f > 1) {
        res <- f * fact_r(f - 1)
        print(res)
    } else {
        res <- 1
        return(res)
    }
    return(res)
}
fact_r(5)