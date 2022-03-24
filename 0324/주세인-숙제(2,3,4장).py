# [2장 4번]
word1 = input("첫 번째 단어 : ")
word2 = input("두 번째 단어 : ")
word3 = input("세 번째 단어 : ")
abbr = word1[0] + word2[0] + word3[0]
print("="*20)
print(f"약자 : {abbr}")

# [3장 1번 A] - 조건문을 이용한 짐의 무게 계산하기
while True :
    weight = int(input("짐의 무게는 얼마입니까? : "))
    if weight < 10 : print("수수료는 없습니다.")
    else :
        print("수수료는 10,000원입니다.")
    if int(input("계속하시겠습니까?(네:1 아니오:0) : ")) == 0 : break

# [3장 1번 B]
while True :
    weight = int(input("짐의 무게는 얼마입니까? : "))
    if weight < 10 : print("수수료는 없습니다.")
    else :
        print("수수료는 {:,}원입니다.".format(weight//10 * 10000))
    if int(input("계속하시겠습니까?(네:1 아니오:0) : ")) == 0 : break

# [3장 2번] - while 반복문을 이용한 숫자 맞추기 게임
import random
print('>> 숫자 맞추기 게임 <<')
com = random.randint(1, 10)

while True :
    my = int(input('예상 숫자를 입력하세요 : '))
    if my > com : 
        print('더 작은 수를 입력하세요')
    elif my < com :
        print('더 큰 수를 입력하세요')
    else :
        print("~~성공~~")
        break

# [3장 3번] - for 반복문을 이용한 수열 출력하기
sum = 0
print(end='수열 = ')
for x in range(1,101) :
    if x % 3 == 0 and x % 2 != 0 :
        print(x,end=' ')
        sum += x
print()
print(f"누적합 = {sum}")

# [3장 4번] - 중첩 반복문을 이용한 단어 카운트하기(word count)
multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
cnt = 0
for x in multiline.splitlines() : 
    for y in x.split() :
        print(y)
        cnt += 1
print(f"단어 개수 : {cnt}")

# [4장 1번] - 다음 lst 변수를 대상으로 각 단계별로 list를 연산하시오
lst = [10,1,5,2]
result = lst*2
print("단계 1 :",result)
result.append(lst[0]*2)
print("단계 2 :",result)
result2 = []
for x in result :
    if result.index(x) % 2 == 1 :
        result2.append(x)
print(result2)

# [4장 2번 A] - list 크기를 키보드로 입력받은 후, 입력 받은 크기만큼 임의의 숫자를 list에 추가하고 list의 크기를 출력
import random
leng = int(input("vector 수 : "))
lst = []
for x in range(leng) :
    num = random.randint(1, 9)
    print(num)
    lst.append(num)
print(f"vector 크기 : {len(lst)}")

# [4장 2번 B] - list 크기를 키보드로 입력받은 후, 입력 받은 크기만큼 임의의 숫자를 list에 추가하고 list의 크기를 출력
                # 이후 list에서 찾을 값을 키보드로 입력한 후 해당값이 list에 있으면 'YES' 없으면 'NO' 출력
import random
leng = int(input("vector 수 : "))
lst = []
for x in range(leng) :
    num = random.randint(1, 9)
    print(num)
    lst.append(num)
print(f"vector 크기 : {len(lst)}")
find = int(input("찾을 값을 입력하세요 : "))
res = True
for x in lst :
    if x == find : 
        print('YES')
        res = False
        break
if res : print('NO')

# [4장 3번 A] - message 변수를 대상으로 'spam'원소는 1, 'ham' 원소는 0으로 dummy변수를 생성하시오 (list+for형식 적용)
message = ['spam','ham','spam','ham','spam']
dummy = []
for x in message :
    if x == 'spam' :
        dummy.append(1)
    elif x == 'ham' :
        dummy.append(0)
print(dummy)

# [4장 3번 B] - message 변수를 대상으로 'spam' 원소만 추출하여 spam_list에 추가하시오
message = ['spam','ham','spam','ham','spam']
spam_list = []
for x in message :
    if x == 'spam' : spam_list.append(x)
print(spam_list)

# [4장 4번] - position 변수를 대상으로 중복되지 않은 직위와 직위별 빈도수를 출력하시오
position = ['과장','부장','대리','사장','대리','과장']
cnt = {}
print("중복되지 않은 직위 :",set(position))
for x in set(position) :
    cnt.update({x:position.count(x)})
print("각 직위별 빈도수 :",cnt)
