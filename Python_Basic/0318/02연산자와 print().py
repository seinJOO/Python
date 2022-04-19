
# 변수 선언
# 1. 변수이름 = 값
# 2. 변수이름1, 변수이름2, 변수이름3 = 값1, 값2, 값3
# 3. 변수이름1 = 변수이름2 = 값1

num1, num2, num3 = 10, 20, 30
print(num1,num2,num3)

su1 = su2 = 100 # 변수에 변수를 넣으면 메모리 저장장소가 같음
print(su1, su2)
print(id(su1),id(su2))

su1 = 200
print(su1,su2)
print(id(su1),id(su2))

su1 = su1 + su2 
print(su1,su2)
print(id(su1),id(su2))

su3, su4 = 200, 200     # 동일한 값은 메모리 저장장소가 같음
print(su3, su4)
print(id(su3),id(su4))

#============================================================

## input()함수 : 문자열을 입력받는 함수 - 반환값은 str(문자열) !!! 
''' print(type(input()))
    print(input("입력 : ")) # 입력값을 문자로 받아서 바로 다시 출력해줌 '''
    
# 문자형 숫자 입력
''' num = input("숫자 입력 : ")
    print('num type : ',type(num))
    print('num = ', num)
    print('num = ',num*2) # 여전히 str '''

# -> 숫자 연산을 위한 정수 형변환
''' num1 = int(input("정수 입력 : ")) # input함수에 형변환해주면 변환이 됨
    print('num1 = ' ,num1 * 2) '''

# -> 숫자 연산을 위한 실수 형변환
''' num2 = float(input("실수 입력 : "))
    result = num1 + num2
    print('result = ', result) '''

# ====>>>> 인자(prompt)에 입력받기 위한 설명을 사용할수 있다.
# input()는 문자열로 입력을 받기 때문에, 숫자로 사용하기 위해서는 필요한 형태로 형변환을 반드시 해야한다.

# input() 예제
# input()을 사용하여 나이와 이름을 입력받아 다음과 같이 출력되게 해주세요.
# => '홍길동'님의 나이는 100세 입니다.
''' name = input("이름 입력 : ")
    age = int(input("나이 : "))
    print("'{}'님의 나이는 {}세 입니다.".format(name, age))
    print(f"'{name}'님의 나이는 {age}세 입니다.")   '''
    
#============================================================

##연산자

# 1. 산술 연산자 : 산술 연산을 위해 사용하는 연산자
#    종류 = "+" , "-", "*", "/", "//"(정수나누기), "%"(나머지), "**"(제곱)
nu1 = 3
nu2 = 2
print(nu1 + nu2)  # 더하기
print(nu1 - nu2)  # 빼기
print(nu1 * nu2)  # 곱하기
print(nu1 / nu2)  # 나누기 결과는 float(실수)으로 반환됨 (1.5)
print(nu1 // nu2) # 정수나누기는 몫만 구함 (1)
print(nu1 % nu2)  # 나머지 (1) -> 데이터 분석 시 가장 자주 사용
print(nu1 ** nu2) # 제곱 (9)

# 2. 비교(관계) 연산자 : 두항의 값을 비교(관계)하여 관계를 설명하는 연산자 ->Bool로 True or False를 반환
#                      값의 기준은 **좌항**
#    "==" : 두항이 값이 같다. "!=" : 두항의 값이 같지 않다. 
#    ">" : 값이 크다. "<" : 값이 작다. 
#    ">=" : 값이 크거나 같다. "<=" : 값이 작거나 같다. 
print(3==3) # True
print(3!=3) # False
print(3>2)  # True
print(3<2)  # False
print(3>=2) # True
print(3<=2) # False

# 3. 논리 연산자 : 두항의 값이 참인지 거짓인지 확인하여 판별하는 연산자-> Bool 로 반환
#    "and"(논리곱) : 두 항의 값이 모두 True인경우 True를 반환, True = 1, False = 0 
#    "or"(논리합) : 두 항 중 하나라도 True인경우에 True 반환 
#    "not"(부정) : True이면 False를 False이면 True를 반환 
print("bool의 int형변환 값은 :",int(True),int(False))
print(0 and 0) #False
print(1 and 0) #False     #and에서는 0이 있으면 무조건 False (이름이 논리곱인 이유 !!)
print(0 and 1) #False
print(1 and 1) #True

print(0 or 0) #False
print(1 or 0) #True     
print(0 or 1) #True
print(1 or 1) #True

print(not 0) #True
print(not 1) #False

# 4. 멤버 연산자 : 왼쪽 피연산자의 값이 오른쪽 연산자 멤버 중 일치 여부를 확인하는 연산자.
#    종류 = in : 왼쪽 피연산자의 값이 오른쪽 피연산자에 존재하는 경우 True 
#          not in : 왼쪽 피연산자의 값이 오른쪽 피연산자에 존재하지 않는 경우 True
print(1 in (1,2,3))     #True
print(1 not in (1,2,3)) #False

# 5. 식별 연산자 : 식별값 비교 연산하여 처리하는 연산자
#   is :  두 피연산자의 식별값(객체타입)을 비교하여 동일 객체라면 True  
#   is not :  두 피연산자의 식별값을 비교하여 동일하지 않은 객체라면 True
num1, num2 = 1 , "1"
print(type(num1) is int)      #True
print(type(num2) is not int)  #True
print(type(num1) is not str)  #True
print(type(num2) is str)      #True

# 6. 비트 연산자 : 비트값을 연산 처리하는 연산자들...
#    종류 = & : 두 비트 and 연산처리하는 연산자 (논리곱)
#          | : 두 비트 or 연산처리하는 연산자 (논리합)
#          ^ : 두 비트에 대한 xor 연산처리하는 연산자 (배타적 논리 합)
#         << : 왼쪽 피 연산자의 비트를 왼쪽으로 오른쪽 숫자만큼 이동
#         >> : 왼쪽 피 연산자의 비트를 오른쪽으로 오른쪽 숫자만큼 이동 

# & : AND 비트 연산
#      00001010(10)
# &    00001101(13)   
#    ===============
#      00001000(8)
print(10 & 13)

# | : OR 비트 연산
#      00001010(10)
# |    00001101(13)   
#    ===============
#      00001111(15)
print(10|13)

# ^ : XOR 비트 연산 - 암호문 처리할 경우에 많이 사용됨
#                    두 비교 비트가 동일하면 0을 반환 / 둘 중 하나라도 1이면 1
#      00001010(10) - 원본
# ^    00001101(13) - 키  
#    ===============
#      00000111(7)  - 암호
# ^    00001101(13) - 키 
#    ===============
#      00001010(10) - 원본
print(10^13)
print(7^13)

# << : 왼쪽 shift 연산자
#      00001010(10)
# <<             3   
#    ===============
#      01010000(80) 
#
# 특징 : 2의 제곱승으로 곱하는 정수 곱하기
print(10<<3)

# >> : 오른쪽 shift 연산자
#      00001010(10)
# >>             3   
#    ===============
#      00000001|(1)010
# 특징 : 2의 제곱승으로 나누는 정수 나누기
print(10>>3) 


'''
문제1. num1, num2, num3 = 5, 15, 27
   위 변수에 할당된 값을 사용하여 다음의 결과가 나오도록
   산술 연산자를 사용 하시오.
      ㄱ. -12
      ㄴ. 75
      ㄷ. 25
      ㄹ. 5.4
      ㅁ. 3.0
'''
num1, num2, num3 = 5, 15, 27
print(num2-num3)
print(num2*num1)
print(num1*num1)
print(num3/num1)
print(num2/num1)

'''
문제2. 다음의 연산자를 보고 True와 False를 구분 하시오. 
      ㄱ. 7 > 18
      ㄴ. 5 < 2
      ㄷ. 6 % 3 > 2
      ㄹ. 5 + 5 != 2 * 5
      ㅁ. True == 1
      ㅂ. 1 == '1'
      ㅅ. 10 // 3 == 10 % 3
      ㅇ. 15 % 4 in (0, 1, 2)
'''
7 > 18              #False
5 < 2               #False
6 % 3 > 2           #False
5 + 5 != 2 * 5      #False
True == 1           #True
1 == '1'            #False
10 // 3 == 10 % 3   #False
15 % 4 in (0, 1, 2) #False

'''
문제3. input()으로 2개의 값을 받은 다음 더하기, 빼기, 곱하기, 나누기 연산을 
    하여 그 결과를 출력하는 코드를 작성하시오.
'''
# a = int(input('a값을 입력하세요'))
# b = int(input('b값을 입력하세요'))
# print(a,b)
# print (a + b)
# print (a - b)
# print (a * b)
# print (a / b)

'''
문제4. 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 출력하는 
    코드를 작성하시오.
    
    비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
    표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9

    출력 예제 : 홍길동님의 비만도는 112.15% 입니다.
'''
# name = input("이름을 입력하세요.")
# height = float(input("키를 입력하세요"))
# weight = float(input("체중을 입력하세요"))

# std = (height - 100) * 0.9 
# bmi = (weight / std) * 100
# print("{}님의 비만도는 {:.2f}%입니다.".format(name,bmi))
