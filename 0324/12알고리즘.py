# 알고리즘 : 어떤 문제를 해결하기 위한 일련의 절차
#          프로그래밍이 로직(논리적인 절차)을 기초로 삼고 있기 때문에 이를 통해 문제를 해결
# 알고리즘의 조건
# 1) 입력 : 외부에서 제공되는 자료가 있을 수 있다
# 2) 출력 : 적어도 한 가지 이상의 결과가 나올 수 있다
# 3) 명백성 : 각 명령들은 애매한 부분 없이 간단 명료해야 한다
# 4) 유한성 : 반드시 종료 조건이 있어야 한다
# 5) 효과성 : 모든 명령들은 명백하고 실행 가능한 것이어야 한다

# 최대값/최소값 (max/min)
# : 전체 자료의 원소들 중에 가장 큰 값과 가장 작은 값을 선별하는 기본 알고리즘

# 입력 자료 생성
import random
dataset = []
for i in range(10) :
    r = random.randint(1, 100)
    dataset.append(r)
print(dataset)

# 변수 초기화
vmax = vmin = dataset[0]

# 최대/최소값 구하기
for i in dataset :
    if i > vmax :
        vmax = i
    if i < vmin :
        vmin = i
print(f"최대값 : {vmax}, 최소값 : {vmin}")

# 정렬(sort) - 선택정렬(오름차순)
dataset = [3,5,1,2,4]
tmp = 0
for i in range(len(dataset)-1) :
    for j in range(i+1,len(dataset)) :
        if dataset[i] > dataset[j] :
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(i+1,"회차 : ",dataset)
print(dataset)

# 정렬(sort) - 선택정렬(내림차순)
dataset = [3,5,1,2,4]
tmp = 0
for i in range(len(dataset)-1) :
    for j in range(i+1,len(dataset)) :
        if dataset[i] < dataset[j] :
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(i+1,"회차 : ",dataset)
print(dataset)

# 검색 (search) 알고리즘 => 순차검색 / 이진검색(이분법)
# 이진검색은 순서대로 정렬되어 있어야한다 !!
dataset = [5,10,18,22,35,55,75,103]
value = int(input("검색할 값 입력 : "))
start = 0               # 시작 위치
end = len(dataset)-1    # 종료 위치
loc = 0                 # 위치값
state = False           # 상태변수

while (start <= end) :
    mid = (start + end) // 2
    if dataset[mid] > value :   # 중앙값이 검색할 값보다 큰 경우
        end = mid - 1
    elif dataset[mid] < value : # 중앙값이 검색할 값보다 작은 경우
        start = mid + 1
    else : 
        loc = mid
        state = True
        break
if state : print(f"찾은 위치 : {loc}번째")
else : print("찾는 값이 없습니다")
        