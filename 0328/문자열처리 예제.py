# [문제 80]
fname = input('이름을 입력해주세요 : ')
print('이름의 길이 :',len(fname))
lname = input('성을 입력해주세요 : ')
print('성의 길이 :',len(lname))
name = fname+' '+lname
print('당신의 fullname은 :',name)
print('fullname의 길이는 :',len(name))

# [문제 81] 각 문자 뒤에 '-'를 붙여 출력하기
subject = input('가장 좋아하는 과목을 입력하세요 : ')
print('-'.join(subject),end='-')

# [문제 82]
# 시 한 구절을 사용자에게 표시하고 시작 인덱스와 마지막 인덱스를 입력받아,
# 입력한 두 값 사이의 문자 출력
string = '이토록 가시가 많으니 곧 장미꽃이 피겠구나'
print(string)
x = int(input('시작 위치를 입력해주세요(1~23) : ')) - 1
y = int(input('마지막 위치를 입력해주세요(~23) : '))
print(string[x:y])

# [문제 83]
# 사용자에게 대문자로 메시지를 입력하라고 요청 후,
# 소문자가 있다면 모두 대문자로 입력할 때까지 계속해서 다시 입력하라고 요청
while True :
    up = input('대문자로 메세지를 입력하세요 : ')
    if up == up.upper() : 
        print('입력한 문자 :',up)
        break
    else : print('모든 문자는 대문자로 입력해야 합니다')
    
# [문제 84]
# 사용자에게 영어 단어를 입력하라고 요청 후, 처음 두 개의 문자만 대문자로 출력
word = input('영어 단어를 입력하세요 : ')
print('입력하신 단어는 :', word.replace(word[0:2], word[0:2].upper()))

# [문제 85]
# 사용자의 이름을 입력하라고 요청한 뒤 이름에 모음이 몇 개인지 출력
name = input('영어이름을 입력하세요 : ')
vowel = ['a','e','i','o','u']
cnt = 0
for x in vowel :
    if x in name :
        cnt += name.count(x)
print('모음의 개수는 ',cnt)

# [문제 86]
# 사용자에게 새로운 비밀번호를 입력 요청하고, 한번 더 입력 요청
# 입력한 두 개의 비밀번호가 일치하면 "Thank you" 출력
# 입력한 문자는 일치하는데 대소문자가 틀리면 "They must be in the same case" 출력
# 문자가 일치하지 않으면 "Incorrect"

pw = input('새로운 비밀번호를 입력하세요 : ')
pwchk = input('새로운 비밀번호를 다시 입력하세요 : ')
if pw != pwchk :
    if pw.lower() != pwchk.lower() : print("Incorrect")
    elif pw.lower() == pwchk.lower() : print('They must be in the same case')
else : print('Thank you')

# [문제 87]
# 단어를 입력하라고 요청한 뒤, 그 단어의 문자를 한 줄에 하나씩 거꾸로 출력하기
word = input('Enter a word : ')
for x in range(len(word)-1,-1,-1) :
    print(word[x])
print('>>>')