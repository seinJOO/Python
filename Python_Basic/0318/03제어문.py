
####제어문(if), 반복문(for,while)

# 제어문(if)

# 단순 if 사용형식 1
# if 조건식 :
#   실행문(종속문장1)
#   실행문(종속문장2)     ==> if 블럭

# -> 조건문이 참일 경우에 종속문장을 실행
# -> 파이썬 에서는 다른 언어와 다르게 들여쓰기가 중요하고, 들여쓰기를 가지고 블럭을 구분함.

''' # 제어문 예제 1
num = int(input("정수입력 : ")) 
if num % 2 == 0 :
    print("num 변수의 값은 짝수입니다.")
    print("num 변수의 값은 2의 배수입니다.")
print("if 다음 문장 실행") '''

''' # 제어문 예제 2 : switch문과 비슷
print("1. Easy Mode")
print("2. Hard Mode")
print("3. Exit")
num = int(input("번호를 선택하세요>>"))
if num ==1 :
    print("Easy Mode Start")
if num ==2 :
    print("Hard Mode Start")
if num ==3 :
    print("Game Exit") '''

''' # 제어문 예제 3 : 3개의 if문을 사용한 것과 같음
su = int(input("수 입력 :"))
if su == 1:
    print("1 입력")
if su > 10:
    print("10보다 큰 값을 입력했습니다.")
if su < 10:
    print("10보다 작은 값을 입력했습니다.") '''

''' # 제어문 예제 4
x = 15
if x > 10 and x != 10: 
    print("x 변수의값은 10보다 크고 ,10과 같지 않다")
if x > 10 or x !=15:
    print("x의 값은 둘중 하나라도 참이면 참으로 결과를 반환") '''

''' # 제어문 예제 5
su = int(input("1~10사이의 정수를 입력하세요. : "))
if su in(1,4,7):
    print("멤버에 있는 숫자입니다.")  '''

# if ~ else : if의 조건식이 참이면 , if의 종속문장을, 그렇지 않으면 else의 종속문장을 실행
# if 조건식 :
#   실행문(종속문장1)
#   실행문(종속문장2)    =>if 블럭
# else :
#   실행문(종속문장1)
#   실행문(종속문장2)    =>else 블럭 둘다 합쳐 하나의 if문으로 처리

# if 활용 예제
''' 
1. 입력한 데이터가 3의 배수인 경우를 출력하시오.
num1 = int(input("숫자를 입력하세요 : "))
if num1 % 3 == 0:
    print(f"입력하신 수({num1})는 3의 배수입니다.")
else :
    print(f"입력하신 수({num1})는 3의 배수가 아닙니다..")
'''
''' 
2. 절대값을 구하는 프로그램을 작성하시오.
num2 = int(input("숫자를 입력하세요"))
if num2 < 0: 
    print(-num2)
if num2 > 0: 
    print(num2) 
'''
'''
3. 수를 입력 받아 짝, 홀수를 구분하여 출력하시오.
num3 = int(input("숫자를 입력하세요"))
if num3 % 2 == 0:
    print("짝수입니다.")
else :
    print("홀수 입니다.")   
'''
'''
4. 두수를 입력받아 큰 수를 출력하시오.
num5 = int(input("첫번째 숫자를 입력하세요"))
num6 = int(input("두번째 숫자를 입력하세요"))
if num5 > num6 :
     print(f"{num5}가 {num6}보다 크다")    
if num5 == num6:
     print("두 숫자는 같습니다.")
if num5 < num6 :
    print(f"{num6}가 {num5}보다 크다") 
'''
'''
5. 세수를 입력받아 큰 수를 출력하시오.
num7 = int(input("첫번째 숫자를 입력하세요"))
num8 = int(input("두번째 숫자를 입력하세요"))
num9 = int(input("세번째 숫자를 입력하세요"))
if num7 > num8 and num7 > num9:
     print("가장 큰 숫자는 첫 번째 숫자인 {}입니다.".format(num7)) 
if num8 > num7 and  num8 > num9 :
    print("가장 큰 숫자는 두 번째 숫자인 {}입니다.".format(num8))
if num9 > num7 and num9 > num8:
     print("가장 큰 숫자는 세 번째 숫자인 {}입니다.".format(num9))
'''
'''
6. 두수를 입력받아 큰수가 짝수이면 출력하시오.
num10 = int(input("첫번째 숫자를 입력하세요"))
num11 = int(input("두번째 숫자를 입력하세요"))
if num10 > num11 and num10 % 2 == 0 :
    print("첫 번째 숫자({})가 더 크며, 짝수입니다.".format(num10))
if num10 < num11 and num11% 2 == 0 :
    print("두 번째 숫자({})가 더 크며, 짝수입니다.".format(num11))
'''
'''
7. 두수를 입력받아 합이 짝수이고 3의 배수인 수를 출력하시오.
num12 = int(input("첫번째 숫자를 입력하세요"))
num13 = int(input("두번째 숫자를 입력하세요")) 
num14 = num12 + num13
if num14 % 2 == 0 and num14 % 3 == 0 :
    print ("두 수의 합({})은 짝수이면서 3의 배수입니다.".format(num14)) 
'''


# 중첩 if 구문 : if구문 안에 if구문을 사용하는 경우
# 다중 if 구문 : if ~ elif~ else 구문으로 if 와 elif 조건을 확인, 부합하면 종속 실행
#               만약 조건에 부합되지 않은 경우에는 else를 실행 

''' # 중첩 if 구문 예제

num1 = int(input("첫번째 정수 입력: "))
num2 = int(input("첫번째 정수 입력: "))
sum = num1 + num2
if sum % 2 == 0:
    if sum % 3 == 0:
        print(f"입력하신 두 수의 합({sum})은 3의 배수이면서 짝수 입니다.")
    else:
        print(f"입력하신 두 수의 합({sum})은 짝수이지만, 3의 배수는 아닙니다.")
else: 
     print(f"입력하신 두 수의 합({sum})은 짝수가 아닙니다.")    '''


''' # 다중 if 구문(if ~ elif ~else) 예제

num = int(input("1~4 중 숫자 하나 입력 : "))
if num == 1 :
    print("1 입력")
elif num == 2 :
    print("2 입력")
elif num == 3 :
    print("3 입력")
elif num == 4 :
    print("4 입력")
else:
    print("잘못 입력했습니다.")'''

'''[Quiz1]
- 사용자로 부터 Gbyte 의 값을 입력받아 byte, kbyte,Mbyte로 각각 출력되게 만드시오.
- (1. byte, 2.kbyte, 3.Mbyte 선택)
- 단위 1024

Gbyte = int(input("Gbyte값을 입력하시오."))
print("1. byte")
print("2. kbyte")
print("3. Mbyte")
num = int(input("번호를 선택하세요>>"))
byte = Gbyte*1024**3
kbyte = Gbyte*1024**2
Mbyte = Gbyte*1024
if num == 1 :
    print(f"{Gbyte}GB의 byte단위는{byte}입니다.")
elif num == 2 :
    print(f"{Gbyte}GB의 kbyte단위는{kbyte}입니다.")
elif num == 3 :
    print(f"{Gbyte}GB의 Mbyte단위는{Mbyte}입니다.")
else :
    print("잘못 입력하셨습니다.")
'''

'''[Quiz2]
- 인증프로그램을 만드시오.
- 아이디가 틀리면 등록되지 않은 아이디입니다 출력
- 비밀번호가 틀리면 비밀번호가 틀렸습니다 출력
- 아이디와 비밀번호가 일치한다면 인증 통과 출력
old_id = 'test'
old_pw = 'python123'
id = input('아이디를 입력하세요')
pw = input('비밀번호를 입력하세요')
if id == old_id :
    if pw == old_pw :
        print('로그인 성공!')
    else :
        print('비밀번호가 틀렸습니다')
else : 
    print('등록되지 않은 id입니다')
'''

# 삼항 조건문 : 조건식이 참인경우와 거짓인 경우 처리할 문장을 한줄로 작성
# 조건식 비교결과에 따라 선택적으로 실행문이 동작합니다.
# (형식)
#  변수 = 참 if (조건문) else 거짓

# 삼항 조건문 예제
num = 9 
result = 0
print("if문==========")
if num >=5:
    result = num * 2
else :
    result = num + 2
print("result = ",result)

print("삼항연산자======")
result2 = num * 2 if num >= 5 else num + 2 # (True실행문 - 조건 - False실행문)
print("result2 = ",result2)

'''
# 문제4. 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 출력하는 
#     코드를 작성하시오.
    
#     비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
#     표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9

#     비만도가 100 미만인 경우 "저체중"
#     비만도가 100~110 사이인 경우 "정상 체중"
      비만도가 110~120 사이인 경우 "과체중"
      비만도가 120~130 사이인 경우 "비만"
      그이상인 경우에는 고모비만으로 표현되게 작성하세요.
      출력예제 : 홍길동님의 비만도는 112.15%로 정상 체중입니다.

name = input('이름을 입력하세요 >> ')
height = float(input('키를 입력하세요 >> '))
weight = float(input('몸무게를 입력하세요 >> '))
std = (height - 100) * 0.9
bmi = weight / std * 100

if bmi < 100 :
    result = '저체중'
elif 100 <= bmi and bmi < 110 :
    result = '정상 체중'
elif 110 <= bmi and bmi < 120 :
    result = '과체중'
elif 120 <= bmi and bmi < 130 :
    result = '비만'
else :
    result='고도비만'

print("{}님의 비만도는 {:.2f}%로 {}입니다.".format(name, bmi, result)) '''