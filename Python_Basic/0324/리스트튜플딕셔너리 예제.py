# [문제 69]
# 다섯 개의 국가 이름을 담고 있는 튜플을 만들고 튜플 전체를 출력하라
# 표시된 국가 이름들 중 하나를 입력하라고 사용자에게 요청하고, 입력된 국가 이름의 인덱스 번호를 출력하라
nations = ('Korea', 'USA', 'France', 'Italy', 'UK')
print(nations)
my = input('위 국가명 중 하나를 입력해주세요 : ')
for x in nations :
    if x == my :
        print("해당 국가의 인덱스 번호 :",nations.index(x))

# [문제 70]
# 사용자에게 숫자를 입력하라고 요청하고, 입력한 위치의 국가 이름이 출력되는 기능을 69번 프로그램에 추가하라
nations = ('Korea', 'USA', 'France', 'Italy', 'UK')

my = int(input('숫자를 입력해주세요(1~5) : '))
print("선택한 국가 :",nations[my-1])

# [문제 71] 두 개의 스포츠 이름을 담고 있는 리스트를 생성하라
# 사용자에게 좋아하는 스포츠가 무엇인지 물어보고 그것을 리스트 끝에 추가하라
# 리스트를 정렬하고 출력하라
sports = ['football','baseball']
my = input('좋아하는 스포츠를 입력하세요 : ')
if my not in sports : sports.append(my)
print(sorted(sports))

# [문제 72] 교과목 여섯 개가 담긴 리스트를 생성하라
# 이들 중 사용자가 좋아하지 않는 과목을 묻고 그 과목을 리스트에서 삭제한 후에 리스트를 다시 출력하라
lst = ['국어','영어','수학','사회','과학','체육']
print(lst)
lst.remove(input('목록 중 싫어하는 과목을 입력하세요 : '))
print(lst)

# [문제 73] 사용자에게 좋아하는 음식 네 개를 입력하도록 요청하고 그것들을 인덱스 번호 1부터 시작하는 딕셔너리에 저장한다.
# 인덱스 번호와 항목이 모두 표시되도록 딕셔너리를 출력한다
# 사용자에게 제거하고 싶은 항목을 묻고 그것을 제거한다
# 남아 있는 데이터를 정렬하고 딕셔너리를 다시 출력하라
foods = {}
tmp = []
print('좋아하는 음식을 네 개 입력하세요')
for x in range(1,5) :
    foods.update({x:input(f"{x}번째 음식을 입력하세요 : ")})
    
print(foods)
my = int(input('목록에서 제거하고 싶은 음식의 번호를 선택하세요 : '))
foods.pop(my)
for x in foods.values() : tmp.append(x)
foods.clear()
for x in tmp : foods.update({tmp.index(x)+1:x})
print(foods)

# [문제 74]
# 열 개의 색상이 담긴 리스트를 생성한다
# 사용자에게 0에서 4 사이의 시작 번호와 5에서 9 사이의 끝 번호를 입력하라고 요청하고, 입력된 시작 번호부터 끝 번호까지의 색상을 출력하라
lst = ['blue','green','yellow','red','orange','black','aqua','purple','navy','beige']
start = int(input('숫자를 입력하세요(0~4) : '))
end = int(input('숫자를 입력하세요(5~9) : '))
print(lst[start:end+1])

# [문제 75]
# 세 자리 숫자 네 개가 담긴 리스트를 생성한다
# 리스트의 각 항목을 한 줄에 하나씩 출력하여 사용자에게 표시한다
# 사용자에게 세 자리의 숫자를 입력하라고 요청한다
# 만약 입력한 숫자가 리스트에 있는 숫자들 중 하나라면 리스트에 그 숫자가 위치한 인덱스를 출력하라
# 그렇지 않다면 "That is not in the list"라는 메세지를 출력하라
lst = [159,642,894]
for x in lst : print(x)
my = int(input('세 자리의 숫자를 입력하세요 : '))
if my in lst : print(lst.index(my))
else : print('That is not in the list')

# [문제 76]
# 사용자에게 파티에 초대할 사람 3명의 이름을 입력하라고 요청하고 리스트에 저장한다
# 모든 이름이 입력되면 추가할 사람이 있는지 묻는다
# 만약 그렇다면 "n"이라고 답할 때까지 이름을 추가하게 한다
# "n"이라고 입력하면 파티에 초대한 사람이 몇 명인지 표시하라
lst = []
for x in range(3) :
    lst.append(input('파티에 초대할 사람의 이름을 입력하세요 : '))
while True :
    chk = input('추가할 사람이 있습니까?(종료:n) : ')
    if chk == 'n' : 
        print(f'파티에 초대된 사람은 {len(lst)}명입니다.')
        break
    else : lst.append(input('파티에 초대할 사람의 이름을 입력하세요 : '))
    
# [문제 77]
# 76번 프로그램을 수정하여 초대할 사람들의 이름이 리스트에 모두 추가되면 전체 명단을 출력하고,
# 리스트에 있는 이름들 중 하나를 입력하라고 요청한다
# 입력된 이름의 위치(인덱스)를 출력하고 그 사람을 정말 파티에 초대할 것인지 묻는다
# "n"이라고 답하면 그 항목을 리스트에서 삭제하고 리스트를 다시 출력한다
lst = []
while True :
    lst.append(input('파티에 초대할 사람의 이름을 입력하세요 : '))
    chk = input('추가할 사람이 있습니까?(종료:n) : ')
    if chk == 'n' : 
        print(lst)
        break
name = input('초대할 사람 중 한 명의 이름을 입력하세요 : ')
chk = input(f"{lst.index(name)}번째 손님 {name}을 정말 파티에 초대하시겠습니까?(y/n) : ")
if chk == 'n' :
    lst.remove(name)
print(lst)


# [문제 78]
# 네 개의 TV 프로그램 타이틀을 담은 리스트를 생성하고 각 항목을 한 줄씩 출력한다
# 사용자에게 다른 프로그램을 입력하도록 요청하고 리스트에서의 원하는 위치를 묻는다
# 입력한 프로그램 타이틀을 원하는 위치에 삽입하고 다섯 개의 TV 프로그램 모두를 다시 출력한다
prgs = ['스물다섯 스물하나','사내맞선','기상청 사람들','애나 만들기']
print(prgs)
prg = input('새로운 프로그램을 입력해주세요 : ')
idx = int(input('어느 위치에 입력할까요?(숫자) : '))
prgs.insert(idx-1, prg)
print(prgs)

# [문제 79]
# 'nums'라는 이름의 빈 리스트를 생성하고, 사용자에게 숫자를 입력하라고 요청한다
# 숫자가 입력되면 그것을 nums 리스트 끝에 추가하고 리스트를 출력한다
# 세 개의 숫자를 입력받으면 마지막 숫자를 저장할 것인지 묻는다
# "n"이라고 답하면 리스트의 마지막 항목을 삭제하고 리스트를 출력하라
nums = []
for x in range(3) :
    nums.append(int(input('숫자를 입력하세요 : ')))
chk = input('마지막 숫자를 저장하시겠습니까?(y/n) : ')
if chk == 'n' :
    nums.remove(nums[len(nums)-1])
print(nums)