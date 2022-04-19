#### 벡터 : 같은 자료형의 연속된 리스트(배열과 비슷)

# 문자 벡터
fruits <- c("banana", "apple", "orange", "mango", "lemon")
fruits[2]   # "apple"

# 숫자 벡터
numbers <- c(13, 3, 5, 8, 22, 16, 7)
numbers[5]      # 5

# 연속된 숫자의 벡터 생성
numbers2 <- 1:10
numbers2         # 1  2  3  4  5  6  7  8  9 10
numbers2[8]      # 8

# 연속된 값의 표현은 정수 단위(1씩)로 증가
numbers3 <- 1.5 : 6.5
numbers3        # 1.5 2.5 3.5 4.5 5.5 6.5

# 연속된 값의 숫자 벡터의 경우 마지막 값이 적합하지 않으면 사용되지 않는다 !!
numbers4 <- 1.5 : 6.4
numbers4        # 1.5 2.5 3.5 4.5 5.5   => 6.5는 출력되지 않음

# 논리값 벡터
log_vals <- c(TRUE, FALSE, TRUE, FALSE)
log_vals    # TRUE FALSE  TRUE FALSE

# 벡터 길이 알아오기(요소 개수 알아오기)
length(numbers4)    # 5

# 벡터의 문자열이나 숫자를 정렬하여 처리하는 함수
sort(fruits)    # 오름차순 정렬
sort(fruits, decreasing = TRUE)  # 내림차순 정렬
sort(numbers)

## 벡터 함수의 사용

# 여러 인덱스 참조 1 : c()
fruits <- c("banana", "apple", "orange", "mango", "lemon")
fruits[c(1, 3, 5)]      # "banana" "orange" "lemon"

# 여러 인덱스 선택 참조 : '-' 로 해당 인덱스의 항목 제외
fruits[c(-1, -3)]      # "apple"  "mango"  "lemon"


# 벡터의 반복 : rep()
# 요소의 반복(each) - rep( 벡터, each = 반복횟수)
repeat_each <- rep(c(1, 2, 3), each = 3)
repeat_each     # 1 1 1 2 2 2 3 3 3

# 벡터의 반복(times) - rep( 벡터, times = 반복횟수)
repeat_times <- rep(c(1, 2, 3), times = 3)
repeat_times    # 1 2 3 1 2 3 1 2 3

# 요소의 개별 반복(times) - rep(벡터, times = 벡터) : 요소 당 반복횟수를 벡터로 각각 지정
#                        요소의 개수와 반복횟수 벡터 요소의 개수가 일치해야함!!!!
repeat_ind <- rep(c(1, 2, 3), times = c(5, 3, 1))
repeat_ind      # 1 1 1 1 1 2 2 2 3


## 순차적인 벡터 생성
# 1
num1 <- 1:10
num1
# 2 seq() 함수 사용 : 인자(from = 시작, to = 끝, by = 단위간격)
num2 <- seq(from = 0, to = 100, by = 20)
num2    # 0  20  40  60  80 100

for (i in seq(from = 0, to = 100, by = 20)) {
    print(i)    # 0  20  40  60  80 100
}

### Lists : list() 함수 사용

# 문자열 리스트
strlist <- list("포도", "바나나", "딸기", "블루베리", "체리")
strlist

# 숫자형 리스트
numlist <- list(10, 20, 30, 40, 50)
numlist

tlist <- list("사과", c(10, 20, 30), "바나나", "체리")
tlist
tlist[2]    # 10 20 30

# 리스트 내 값 참조
strlist <- list("사과", "바나나", "체리")
"사과" %in% strlist     # TRUE

# 리스트 내에 값 추가 : append() - 원래 변수의 값은 변하지 않음
strlist <- append(strlist, "메론", after = 2)
strlist     # "사과", "바나나", "메론", "체리"

strlist <- append(strlist, "블루베리")
strlist     # "사과", "바나나", "메론", "체리", "블루베리"

# 리스트 내에 값 제거
strlist <- strlist[-1]
strlist     # "바나나", "메론", "체리", "블루베리"

# 리스트 인덱스 범위 내의 값을 출력
strlist     # "바나나", "메론", "체리", "블루베리", "블루베리", "블루베리", "블루베리"
strlist[1:4]    # "바나나", "메론", "체리", "블루베리"

# 리스트 결합 - 벡터로 결합시키기
list1 <- list("a", "b", "c")
list2 <- list(1, 2, 3)
list3 <- c(list1, list2)
list3   # "a", "b", "c", 1, 2, 3
