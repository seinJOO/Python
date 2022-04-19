import os
# os 모듈은 파이썬에서 제공하는 기본 라이브러리 모듈
# os와 관련된 함수들이 저장된 모듈
# system() => os의 시스템 명령어를 사용할 수 있게 함

import time # 시간과 관련된 기능을 제공하는 기본 라이브러리 모듈

# os.system('cls')     # 모듈.함수 => 직접 참조 연산자

# 랜덤 함수 : 임의의 값을 출력하는 함수 (난수 : 생성된 임의의 값)
# 랜덤 함수를 사용하기 위해 모듈을 사용 : random

# 모듈 사용 방법 : import [모듈명]
# 1) import random     # 랜덤 모듈 전체를 로딩
# 2) from [모듈] import [모듈에 있는 내용] -> 모듈 내에 일부 정보를 로드
#    import random[모듈] import random[함수] -> 랜덤 모듈 내에 random() 함수를 로드

# 두 방식은 기능 사용방식에 차이가 존재함
# 1) import [모듈] => [모듈명].[사용할 값]
#    ex. import random; => random.random()
# 2) from [모듈] import [모듈 사용값] => [모듈 사용값]을 그대로 사용
#    ex. from random import random; => random()

from random import random
print(random()) # random모듈에 있는 random()은 0.0~1.0미만의 임의의 값을 출력(float)

# 0.0~10.0 미만의 임의의 값을 출력(float)
print(random()*10)
# 0~10 미만의 임의의 값을 출력(int)
print(int(random()*10))
# 1~10까지의 값을 출력(int)
print(int(random()*10)+1)

# 예제1) 1~45 까지의 임의의 수 출력
print("예제 1 =======")
for x in range(6) :
    print(int(random()*45)+1,end=" ")
print()
# 문제1) 1~100 까지의 랜덤 값을 6개 출력하는 코드 작성
print("문제 1 =======")
x=0
for x in range(6) :
    print(int(random()*100)+1,end=" ")
print()
# 문제2) 1~100 까지의 랜덤 값을 반복하여 출력하되, 출력 값이 50이 출력되는 순간 반복 종료
print("문제 2 =======")
while True :
    num = int(random()*100)+1
    print(num,end=' ')
    if num == 50 : break
print()
# 문제3) 1~15까지 랜덤 값을 중복 없이 3개 생성하여 출력하는 코드
print("문제 3 =======")
x=0 ; num = int(random()*15)+1; rnd=[]
while rnd.__len__() < 3 :
    while num in rnd :     
        num = int(random()*15)+1
    rnd.append(num)
print(rnd)
print()


# random 모듈 내에 있는 다른 형태의 random 함수들
# - randint() : 임의의 값을 출력하는 int값 랜덤 함수
# 사용방법
#   randint(a,b) => a : 시작값, b : 마지막값 -> 시작값부터 마지막값까지의 랜덤

# 예시 - 1~6까지의 임의의 값 출력
from random import randint
print(randint(1,6))

# - randrange() : 범위 내에 있는 임의의 값을 출력
# 예시1) randrange(5,10) => 5~10 미만의 값을 출력(5,6,7,8,9)
# 예시2) randrange(5,10,2) => 5~10 미만까지 범위 중 2씩 증가 값을 출력(5,7,9)

# 예시3)
from random import randrange
print(randrange(10))
print(randrange(5,10))
print(randrange(5,10,2))

# random 모듈 내에 choice()함수
#   : 리스트와 같은 형태의 자료 중 일부를 랜덤하게 추출하는 함수
# 예시)
# dice = [1,2,3,4,5,6]  -> 리스트형
# choice(dice)  -> dice 리스트 내에 있는 멤버 중 하나를 추출하여 출력

# 예시4-1)
import random
dice = [1,2,3,4,5,6]
st = 'Hello World!'
x = random.choice(dice)
y = random.choice(st)
print("dice에서 출력된 값 : ",x)
print("st에서 출력된 값 : ",y)

# 예시4-2)
from random import choice
dice = [1,2,3,4,5,6]
st = 'Hello World!'
x = choice(dice)
y = choice(st)
print("dice에서 출력된 값 : ",x)
print("st에서 출력된 값 : ",y)

# 문제4) 1~99까지 랜덤 값 중에 짝수는 True, 홀수는 False를 출력하는 프로그램 코딩
from random import randrange
rand = randrange(1,99)
if rand % 2 == 0 : print(rand,"= True")
else : print(rand,"= False")

'''
ASCII코드 : 미국 표준 문자 코드, 통신 상 기본 문자 코드로 사용 중
            7bit(0~127)로 하나의 문자를 표현할 수 있음
특징 1) 프린트 가능한 문자 95개, 프린트 불가능한 문자 33개 
                => 프린트 가능한 문자의 시작 0x20(32) -> "공백"부터 시작, 0x7e(126)까지
    2) 숫자는 0x30(48)='0' 에서부터 0x39(57)='9'까지의 값을 가진 10개 코드
    3) 영문 대문자는 0x41(65) = 'A' => 0x5a(90)='Z'까지
    4) 영문 소문자는 0x61(97) = 'a' => 0x7a(122) = 'z'까지
    5) ASCII코드는 문자이지만 숫자(정수)로 표현이 가능함
    
숫자를 문자(ASCII)로 변경하는 함수 chr() : ()안에 코드값을 전달하면 그 값을 문자로 출력 '''
print(chr(65))
print(chr(0x41))

# [문제5] 'A'~'Z'까지의 임의의 문자 3자리를 출력하는 코드 작성
from random import randrange, random, randint, choice
x=0; num=0; nums=[]
while nums.__len__() <= 3 :
    while num in nums :
        num = randrange(65,91)
    nums.append(num)
    print(chr(num),end=' ')