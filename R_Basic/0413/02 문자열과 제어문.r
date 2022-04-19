
## 문자열
# 1. 문자열
str <- "Hello R!!"
print(str)

# 2. 여러줄 문자열
str2 <- "You will find information 
on some of the sources 
for this book in appendix four."
print(str2) # "You will find information \non some of the sources \nfor this book in appendix four."                #nolint

# 3. 입력데이터와 동일하게 "\n"이 줄바꿈으로 표현되도록 출력하고 싶다면 cat()
cat(str2)


# 4. 문자열 길이 : nchar(str)
nchar(str)      # 9
nchar(str2)     # 82

# 5. 문자열 내에 글자 확인 함수 : grepl()
str3 <- "Hello World!! Hi, R~"
grepl("H", str3)        # TRUE
grepl("lo Wo", str3)    # TRUE
grepl("Hallow", str3)   # FALSE

# 6. 문자열의 결합 : paste()
str4 <- "Hello"
str5 <- "R~~~"

paste(str4, str5)

## escape 문자 : \\, \n, \r : 현재 줄 맨 앞으로 커서 이동, \t, \b

## 조건문 : if - java와 동일, 중첩 가능
# if (조건1) {
#     조건1 실행문
# } else if (조건2) {
#     조건2 실행문
# } else {
#     else조건 실행문
# }

## x가 10일 경우, if문을 사용하여 2의 배수이면 "2의 배수", 2의 배수이면서 6의 배수면 "6의 배수"
x <- readline("숫자를 입력하세요 : ")       # R에서 입력값을 받는 법 (한 줄씩 실행 !!!!!)
x <- as.numeric(x)
if (x %% 2 == 0) {
    print("2의 배수")
    if (x %% 6 == 0) {
        print("6의 배수")
    }
} else {
    print("x는 2나 6의 배수가 아닙니다")
}

## 반복문 : while, for
# next(=continue), break                                                          # nolint
i <- 0
while (i < 6) {
    i <- i + 1
    if (i == 3) {
        next        # = continue
    }
    print(i)        # 출력결과 : 1 2 4 5 6
}

# 무한루프
j <- 0
while (TRUE) {
    j <- j + 1
    if (j == 3) {
        break
    }
    print(j)        # 출력결과 : 1 2
}

## for문
dice <- c(1, 2, 3, 4, 5, 6)
for (x in dice) {
    print(x)        # 출력결과 : 1 2 3 4 5 6
}

for (x in 1:6) {
    print(x)        # 출력결과 : 1 2 3 4 5 6
}

x <- 1
for (i in 2:5) {
    x <- x * i
    print(x)    # 출력결과 : 2 6 24 120 (2*3*4*5)
}