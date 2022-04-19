### Factors (factor()) : 범주형 자료일 때 사용
## 정해진 범위 내에서 카테고리별로 분석을 하기 위해 사용되는 데이터 자료형
## 예) 성별 : 남성,여성 / 음악 : 록, 팝, 클래식, 재즈 / 운동 : 스테미나, 근력

# factor 생성
m_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"))                #nolint
m_genre

# levels() : 카테고리를 출력 (중복값 제거하고 출력)
levels(m_genre)     # "Classic" "Jazz"    "Pop"     "Rock"
length(m_genre)             # 8
length(levels(m_genre))     # 4

# factor 요소로 접근
m_genre[3]      # Classic / Levels: Classic Jazz Pop Rock => 해당 인덱스 값과 팩터의 범주를 함께 보여줌         #nolint

# 요소의 변경
m_genre[3] <- "Pop"
m_genre[3]      # Pop

## 주의) factor는 정해진 범주 내에서 카테고리별로 분석을 위해 사용 -> 사전에 정의되어 있지 않은 값으로 변경 시 에러 발생
# m_genre[3] <- "Opera"  오류 : 요인의 수준(factor level)이 올바르지 않아 NA가 생성되었습니다.

m_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"),                 #nolint
levels = c("Classic", "Jazz", "Pop", "Rock", "Opera"))
m_genre[3] <- "Opera"
m_genre[3]


### 순열과 조합
## 순열 : 서로 다른 n개중에 r개를 선택하여 줄을 세우는 경우의 수 -> 순서를 고려한다

## 팩토리얼(서로 다른 n개를 나열하는 경우의 수) 구하기
fact <- function(n) {
    x <- 1
    for (i in 2:n) {
        x <- x * i
    }
    return(x)
}
fact(5)

# ============================================
# 5개 중 2개를 추출하는 순열
x <- c(1, 2, 3, 4, 5)
count <- 0
for (i in 1:5) {
    x2 <- x[x != i] # i에 저장된 값 제외하고 x2에 저장
    print(x2)
    for (j in 1:4) {
        print(c(i, x2[j]))
        count <- count + 1
    }
}
print(count)

# 순열 공식 => nPr = n! / (n-r)!
perm <- function(n, r) {
    return(fact(n) / fact(n - r))
}
perm(5, 2)

### 조합 : 서로 다른 n개중에 r개를 선택하는 경우의 수 -> 순서를 고려하지 않음
## 조합 공식 nCr = nPr / r! = n! / (n-r)!r!
# *** 조합 함수 : choose(n,r)

## 순열에서 같은 값으로 이루어진(중복) 경우를 제거하기 위해 선택한 개수만큼의 팩토리얼로 나눠줌
# 123 132 213 231 312 321 : 순열 = 3! = 6가지 , 조합 = 3!/3! = 1가지

# 5개 중 2개를 추출하는 조합
x <- c(1, 2, 3, 4, 5)
count <- 0
for (i in 1:4) {     # 두 개의 수를 추출하기 때문에 5는 포함하지 않는다! 아래에서 남은 숫자를 하나 더 뽑을거기 때문 !!
    for (j in (i + 1):5) {
        print(c(i, j))
        count <- count + 1
    }
}
print(count)

# 공식으로 풀어보기
comb <- function(n, r) {
    return(fact(n) / (fact(n - r) * fact(r)))
}
comb(45, 6)

### 순열, 조합, 상트페테르부르크의 역설