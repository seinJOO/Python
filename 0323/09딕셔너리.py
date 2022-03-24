# 딕셔너리(Dictionary)
# 1. List와 비슷한 자료형. List는 요소(멤버)에 대한 접근 시 첨자(index)를 사용
# 2. 딕셔너리도 첨자를 사용 - "key"
# 3. 딕셔너리는 key가 가리키는 곳에 값(=value=데이터)이 존재함   * key 사용의 장점 1) 빠른 탐색 2) 사용하기 편리
# 4. 딕셔너리를 정의할 때는 "{}"를 사용함
# 5. 특정 슬롯에 대해서 참조할 때 key-value를 입력하거나, 딕셔너리 안에 있는 요소를 참조할 경우 "[]"를 사용
# 6. 슬라이싱(slicing)이 불가하다 !! 첨자(key)가 일정한 연속된 값을 가지지 않기 때문

# (형식)
# 변수명 = {}  => 비어있는 딕셔너리 선언
# 변수명 = {key1:value1, key2:value2, key3:value3,...}

# dict()를 이용해서 선언하는 경우 *****
# 변수명 = dict([(k1,v1),(k2,v2),(k3,v3),...])

# (접근방식)
# dic = {key:value}
# dic[key] = value
# print(dic[key])  => 출력결과 : value

# 형식 예시
print(dict([('a',100),(1,'test')]))
dic = {'a':100, 1:'test'}
print(dic['a'])     # 100
print(dic[1])       # 'test'

# 예제 1) 딕셔너리에 대한 정의 및 접근방법
dic = {'a':1,'b':2,'c':3}
print(dic['c'])     # 3
dic['c'] = dic['b'] * 5     # 'b'의 value값 2 * 5 = 10이 'c'의 value값으로 들어감
print(dic)          # {'a': 1, 'b': 2, 'c': 10}
dic['d'] = 100              # 동일한 key값이 없다면 자동으로 추가됨
print(dic)          # {'a': 1, 'b': 2, 'c': 10, 'd': 100}

# 예제 2) 딕셔너리에 for문을 사용하는 경우
print(dic)
for k in dic :
    print(k, end=' / ')     # key값이 출력됨
    print("key값 : {}, key를 이용한 참조값 : {}".format(k,dic[k]))
print()

# 예제 3) 딕셔너리와 리스트를 같이 사용하는 경우 (딕셔너리 안의 값(value)을 리스트로 사용)
    # => 카테고리화
dl = {'음료':['탄산','과일','우유','물'],
      '식사':['김밥','라면','돈까스','비빔밥']}

for key in dl :
    print("형식 1")
    print(key, end=' : ')   # 음료 : 
    for i in dl[key] :
        print(i, end=' ')   # 탄산 과일 우유 물 
    print() 
       
    print("형식 2")
    print(key, end=' : ')
    for j in range(4) :
        print(dl[key][j],end=' ')
    print()
    
# 예제 4-1) 리스트 안에 딕셔너리가 있는 경우
ld = [{'name':'홍길동','age':18,'bloodType':'A'},
      {'name':'이방원','age':24,'bloodType':'B'}]
for dic in ld :     # 딕셔너리 하나씩 출력
    print(dic['name'],dic['age'],dic['bloodType'])
    
# 예제 4-2) 딕셔너리 안에 딕셔너리가 있는 경우
dd = {'홍길동' : {'age':18,'bloodType':'A'},
      '이방원' : {'age':24,'bloodType':'B'}}
for name in dd :    # key값 하나씩 출력
    print(name, dd[name]['age'],dd[name]['bloodType'])      # 홍길동 18 A ..
    
# Dictionary에 사용하는 함수들
# update(dict) : 사전형 자료에 값을 추가 (key:value) => 인자값을 dict형태로 받아야 함
# fromkeys(iter[,value]) : iter에 리스트, 튜플의 값을 딕셔너리의 키로 사용하는 딕셔너리를 생성하여 반환 (값들을 가져와서 key로 사용)
# get(key[,value]) : 사전형의 키를 사용하여 값을 얻어오는 함수
# keys() : 사전형 자료에서 모든 키를 반환하는 함수
# values() : 사전형 자료에서 모든 값을 반환하는 함수
# items() : 사전형의 모든 "키(key):값(value)"의 쌍으로 튜플(*)로 반환
# pop(key) : 사전형 자료의 키를 통해서 값을 반환한 후에 삭제
# popitem() : 사전형 자료의 마지막 "키:값" 쌍을 튜플(*)로 반환 후 삭제
# clear() : 사전형의 모든 "키:값"을 삭제하여 빈 사전형 자료로 만듬

# update()
dic = {'a':1,'b':2,'c':3}
dic.update({'d':4})
print(dic['a'])
print(dic['d'])
print(dic)          # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# fromkeys(iter, value)
ke = ['a','b','c','d']
dic1 = {}.fromkeys(ke)      
dic2 = {}.fromkeys(ke,1)    
print(dic1)                 # {'a': None, 'b': None, 'c': None, 'd': None}
print(dic2)                 # {'a': 1, 'b': 1, 'c': 1, 'd': 1}

# get(key[,value]) **
dic = {'a':1,'b':2,'c':3}
value = dic.get('b')
print(value)
print(dic)
print("key가 d인 값 출력 :",dic.get('d'))                 # key가 d인 값 출력 : None             
                                                         # 찾으려는 값이 존재하지 않으면 기본적으로 'None' 출력
print("key가 d인 값 출력 :",dic.get('d','Not exist key')) # key가 d인 값 출력 : Not exist key     
                                                         # 값을 찾으면 value값을, 찾지 못하면 문자열 지정하여 출력
print("key가 c인 값 출력 :",dic.get('c','Not exist key')) # key가 c인 값 출력 : 3

# keys() - key값만 추출할 때 사용
dic = {'a':1,'b':2,'c':3}
for key in dic.keys() : print(key,end=' ')      # a b c 
print()
print(type(dic.keys()))     # <class 'dict_keys'> => 데이터 형태가 따로 존재함..!!
print(dic.keys())           # dict_keys(['a', 'b', 'c'])

# values() - value값만 추출할 때 사용
dic = {'a':1,'b':2,'c':3}
for values in dic.values() :
    print(values,end=' ')   # 1 2 3 
print()
print(type(dic.values()))   # <class 'dict_values'> => 데이터 형태가 따로 존재함..!!
print(dic.values())         # dict_values([1, 2, 3])

# items() - unpacking 할 때 사용 (key값과 value값 모두 사용하고자 할 때)
dic = {'a':1,'b':2,'c':3}
for key, value in dic.items() :
    print("{}:{}".format(key,value),end='\t')   
                    # 출력 : a:1	b:2    c:3
print()

# pop(key)
dic = {'a':1,'b':2,'c':3}
value = dic.pop('b')    
print(value)            # 2
print(dic)              # {'a': 1, 'c': 3}

# popitem()
dic = {'a':1,'b':2,'c':3}
tu1 = dic.popitem()
print(dic)      # {'a': 1, 'b': 2}
print(tu1)      # ('c', 3) => 튜플로 저장됨

# clear()
dic = {'a':1,'b':2,'c':3}
print(dic)
dic.clear()     # {'a': 1, 'b': 2, 'c': 3}
print(dic)      # {}


# [문제 1]
# 이름, 전화번호, 이메일 주소를 키로 사용하는 사전 자료를 생성하시오
dic = {'이름' : '주세인' , '전화번호' : '01026102291', '이메일주소' : 'senny@zzang.com'}
print(dic)

# [문제 2]
# 리스트형 변수에 1번 문제와 같은 사전 자료가 여러 개 생성될 수 있게 하시오 (입력값을 받아서)
pbook = [] ; menu = 1
while menu != 0 :
    dic2.update('이름',input("이름을 입력하세요 : "))
    dic2.update('전화번호',input("전화번호를 입력하세요 : "))
    dic2.update('이메일주소',input("이메일을 입력하세요 : "))
    menu = int(input("계속 추가하시려면 1, 종료하시려면 0을 입력하세요 >> "))   


# [문제 3]
# 2번에서 입력한 자료가 출력될 수 있도록 하시오
for x in pbook :
    for key, value in x.items() :
        print("{} : {}".format(key, value))
        
# ==복습==

# [문제1] 변수명 menu로 사전형 자료를 만들어보기
menu = {'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}
for key, value in menu :
    print(key,"({}원)".format(value))
    
# [문제2] 위에서 만든 사전형 자료에서 가격이 6000원 미만에 해당하는 메뉴와 가격을 출력하는 코드 작성
menu = {'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}
for key, value in menu.items() :
    if value < 6000 :
        print("{}({}원)".format(key,value))

# 선생님 답
for ke in menu :
    if menu[ke] < 6000 :
        print(f"{ke}:{menu[ke]}원")

# [문제3] 사용자 입력으로 메뉴와 가격을 입력받아 menu변수에 자료를 추가하기 (동일한 메뉴는 가격만 변경)
# [문제4] 메뉴를 자동으로 선택하여 출력
menu = {'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}
while True :
    newMenu = input('추가할 메뉴를 입력하세요 : ')
    newPrice = int(input('가격을 입력하세요(숫자만) : '))
    menu.update({newMenu:newPrice})   
    if int(input("메뉴를 출력하시겠습니까 ?(네 : 1 / 아니오 : 0)")) == 1 :
        print("=====메뉴판=====")
        for key, value in menu.items() :
            print(key,"({}원)".format(value))
        print("================") 
    if (int(input('메뉴를 더 추가하시겠습니까 ?(추가 : 1 / 종료 : 0) :'))) == 0 : break

# 선생님 답
while True :
    newMenu = input('추가할 메뉴를 입력하세요 : ')
    newPrice = int(input('가격을 입력하세요(숫자만) : '))
    if newMenu in menu :
        menu[newMenu] = newPrice
        print("{}의 가격이 변경되었습니다".format(newMenu))
    else : 
        menu.update({newMenu:newPrice})
        print("{} 메뉴가 추가되었습니다".format(newMenu))
    if int(input("메뉴를 출력하시겠습니까 ?(네 : 1 / 아니오 : 0)")) == 1 :
        print("=====메뉴판=====")
        for key, value in menu.items() :
            print(key,"({}원)".format(value))
        print("================") 
    if (int(input('메뉴를 더 추가하시겠습니까 ?(추가 : 1 / 종료 : 0) :'))) == 0 : break
        