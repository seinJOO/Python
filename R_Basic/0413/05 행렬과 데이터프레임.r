### Matrix(행렬) - matrix()를 사용, nrow, ncol 값으로 정렬 지정
# 데이터는 첫 컬럼부터 순서대로 채움 !!

## 행렬생성 1
rmat <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 3)
rmat    # 행이 3개인 행렬 완성
cmat <- matrix(c(1, 2, 3, 4, 5, 6), ncol = 3)
cmat    # 열이 2개인 행렬 완성
rcmat <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 3, ncol = 2)
rcmat   # 행이 3개, 열이 2개인 행렬 완성

## 행렬생성 2
mat <- matrix(c("blueberry", "buzzy", "cherry", "melon"), nrow = 2, ncol = 2)
mat

## 행렬에 대한 접근 : "[]"를 이용
mat[1, 2]    # "cherry" : 1행 2열 데이터 출력
mat[2, ]     # "buzzy" "melon" : 두번째 행 모두 출력
mat[, 2]     # "cherry", "melon" : 두번째 컬럼 모두 출력
mat[, ]       # 행렬 모두 출력

## 하나 이상의 행렬에 접근
mat2 <- matrix(c("blueberry", "buzzy", "cherry", "melon", "grape",
"orange", "pineapple", "grapefruit", "lemon"), nrow = 3, ncol = 3)
mat2
mat2[c(1, 2), ]  # 3행 제외하고 출력
mat2[, -3]       # 3열 제외하고 출력

## 행렬에 값을 추가 (열 추가) : cbind(추가할 행렬, 추가할 데이터) => 행 개수 맞춰야함!!
mat3 <- cbind(mat2, c("strawberry", "raspberry", "blackberry"))
mat3

## 행렬에 값을 추가 (행 추가) : rbind(추가할 행렬, 추가할 데이터) => 열 개수 맞춰야함!!
mat4 <- rbind(mat2, c("strawberry", "raspberry", "blackberry"))
mat4

## 행렬 값 제거 : 음수 인덱스 표시
rrmat <- mat3[-c(1, 2), c(-3)]  # 1행, 2행, 3열 제거
rrmat

## 행렬 값 확인
"apple" %in% mat4       # FALSE
"blueberry" %in% mat4   # TRUE

## 행렬의 row와 column 알아오기 : dim()
mat3
dim(mat3)       # 3 4 : row 3, col 4
dim(mat3)[1]    # 행 개수 알아오기
dim(mat3)[2]    # 열 개수 알아오기

## 행렬의 길이
length(mat3)    # 12 : 3 x 4

# 예제 : 행렬에 반복문을 사용하여 rows와 column 값으로 행렬값을 불러오세요
tmat <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)

for (ro in 1:dim(tmat)[1]) {
    for (co in 1:dim(tmat)[2]) {
        print(tmat[ro, co])
    }
}

for (ro in 1:nrow(tmat)) {
    for (co in 1:ncol(tmat)) {
        print(tmat[ro, co])
    }
}

## 행렬 합치기
matr1 <- matrix(c("apple", "banana", "cherry", "grape"), nrow = 2, ncol = 2)
matr2 <- matrix(c("orange", "mango", "pineapple", "guaba"), nrow = 2, ncol = 2)

# row로 더하기 : rbind()
mat_combined <- rbind(matr1, matr2)
mat_combined
dim(mat_combined)       # 4행 2열

# column으로 더하기 : cbind()
mat_combined <- cbind(matr1, matr2)
mat_combined
dim(mat_combined)       # 2행 4열


### Arrays 배열
tarr <- c(1:24) # 1 ~ 24 순차적으로 입력
tarr # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
class(tarr)     # "integer"

# array(기준array, dim = c(행 개수, 열 개수, 행렬 개수))
multiarr <- array(tarr, dim = c(4, 3, 3)) # 4행 3열(길이 12)의 행렬 3개 만들기
multiarr    # (1~12, 13~24, 1~12 데이터를 가진 3개의 행렬 생성) - 데이터가 부족하면 반복함

# arrays 값 접근 - [행 위치, 열 위치, 추출 대상 매트릭스 위치]
multiarr[1, 2, 2]   # multiarr의 2행 2열, 두번째 매트릭스 데이터 추출

# c() 함수를 이용한 접근
multi2arr <- array(tarr, dim = c(4, 3, 2))
multi2arr[1, , 1]       # 첫번째 행만, 첫번째 매트릭스에서 추출
multi2arr[, c(1), 1]    # 첫번째 열만, 첫번째 매트릭스에서 추출

# 존재 여부
3 %in% multi2arr     # TRUE

## row와 column 확인
dim(multi2arr)      # 4 3 2 : 행개수, 열개수, 매트릭스개수

## array 길이
length(multi2arr)   # 24 : 4 x 3 x 2

## 반복문 사용
for (x in multiarr) {
    print(x)
}

### Data Frames (data.frame())
## 데이터 프레임은 데이터를 테이블 형태로 표현하는 자료형
## 데이터 프레임 안의 데이터 타입은 서로 달라도 된다!

## 첫번째 컬럼은 문자(character), 두 번째 컬럼은 숫자(numeric), 세 번째 컬럼은 logical로 생성
dframe <- data.frame(       # tag = value 형식으로 각 컬럼을 입력
    Training = c("Strength", "Stemina", "Other"),
    Pulse = c(100, 150, 120),
    Duration = c(TRUE, FALSE, TRUE)
)

dframe

## summary() : 데이터프레임 값을 요약해서 출력(파이썬의 info())
summary(dframe)
    #    Training             Pulse        Duration
    #  Length:3           Min.   :100.0   Mode :logical
    #  Class :character   1st Qu.:110.0   FALSE:1
    #  Mode  :character   Median :120.0   TRUE :2
    #                     Mean   :123.3
    #                     3rd Qu.:135.0
    #                     Max.   :150.0
## 데이터프레임도 태그명, 인덱스, $로 접근 가능 !
dframe[1]
dframe["Pulse"]
dframe$Duration

## row 추가 : rbind()
dframe <- rbind(dframe, c("Speed", 110, TRUE))
dframe
dframe <- cbind(dframe, steps = c(6000, 1000, 8900, 9000))
dframe

## row와 column 제거
deframe <- dframe[-c(1), -c(1)]     # 1행 전체, 1열 전체 제외
deframe

## ncol(), nrow()
ncol(dframe)        # 4행
nrow(dframe)        # 4열

## 요소 개수(길이)
length(dframe)      # dataframe의 size는 Series 개수로 판단 -> 4개의 열 = 4개의 시리즈 = 길이 4

## 행 결합 rbind() - 행 붙이기 -> 열 개수가 같아야 함 !!
df1 <- data.frame (
    Training = c("Strength", "Stemina", "Other"),
    Pulse = c(100, 150, 120),
    Duration = c(TRUE, FALSE, TRUE)
)

df2 <- data.frame(
    Training = c("Stemina", "Stemina", "Strength"),
    Pulse = c(140, 150, 160),
    Duration = c(FALSE, FALSE, TRUE)
)

df3 <- rbind(df1, df2)
df3

## 열 결합 cbind() - 열 붙이기 -> 행 개수가 같아야 함 !!

df4 <- data.frame(
    Training = c("Strength", "Stemina", "Other"),
    Pulse = c(100, 150, 120),
    Duration = c(TRUE, FALSE, TRUE)
)
df5 <- data.frame(
    Steps = c(3000, 6000, 2000),
    Calories = c(300, 400, 300)
)

df6 <- cbind(df4, df5)
df6