
'''
[문제1] 윤년 구하기
윤년을 구하는 코드를 작성하시오
4의 배수는 윤년이 된다. 그 외는 평년
4의 배수이면서 100의 배수인 경우는 평년이다. 그 외는 윤년
4 그리고 100의 배수이면서 400의 배수인 경우 윤년이다. 그 외는 평년

출력 예제 : 2017년은 평년입니다.
'''
print("윤년 계산기==============")
year = int(input("연도를 입력하세요 >>>"))
if year % 4 == 0 :
    if year % 100 & year % 400 :
        result = '윤년'
    else :
        result = '평년'
else :
    result = '평년'
    
print(f"{year}년은 {result}입니다.")

# 문제 2
# 이름, 학번, 국/영/수 세 과목의 성적을 입력받아 합계와 평균을 구하고
# 평균이 90이상이면 'A', 80이상 'B', 70이상 'C', 60이상 'D', 60미만이면 'F'를 출력하시오
print("학생정보 출력=============")
name = input("이름을 입력하세요 >>> ")
number = int(input("학번을 입력하세요 >>> "))
kor = float(input("국어 성적을 입력하세요 >>> "))
math = float(input("수학 성적을 입력하세요 >>> "))
eng = float(input("영어 성적을 입력하세요 >>> "))
total = kor + math + eng
avg = total / 3
if avg >= 90 :
    result2 = 'A'
elif avg >= 80 :
    result2 = 'B'
elif avg >= 70 :
    result2 = 'C'
elif avg >= 60 :
    result2 = 'D'
else :
    result2 = 'F'
print(f"{name}님({number})의 학점은 {result2}입니다.")
print("합계 : ","{:.2f}".format(total),"\t 평균 : ","{:.2f}".format(avg))

# [문제3]
# 커피의 개당 가격은 2000원이다. 10개를 초과하면 초과하는 양에 대해서만 개당 1500원씩 받는다.
# 커피의 개수를 입력받아 금액을 출력하시오

coffee = int(input("커피 개수를 입력하세요 >>> "))
if coffee > 10 :
    price = (coffee - 10) * 1500 + 20000
else :
    price = coffee * 2000
print(f"총 금액은 {price}입니다.")

'''
문제4
정수를 입력받아 아래와 같이 출력하시오
3의 배수이면서 4의 배수입니다 / 3의 배수입니다 / 4의 배수입니다
3의 배수도, 4의 배수도 아닙니다 / 0은 3의 배수도 4의 배수도 아닙니다
'''
num = int(input("정수를 입력하세요 >>> "))

if num == 0 :
    print(num,'은 3의 배수도 4의 배수도 아닙니다')
elif num % 3 == 0 :
    if num % 4 == 0 :
        print(num,'은 3의 배수이면서 4의 배수입니다')
    else :
        print(num,'은 3의 배수입니다')
elif num % 4 == 0 :
    print(num,'은 4의 배수입니다')
else :
    print(num,'은 3의 배수도, 4의 배수도 아닙니다')

# -> 다중 if문을 사용하여 여러 조건식을 만들 경우 범위가 작은 조건식을 먼저 정의하기 !!!!
