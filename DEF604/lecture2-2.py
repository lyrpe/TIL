
#Excercise : Dead Code 작성 주의!!


#Exception Handling  : try/except 문 사용

astr = 'Hello bob'
#istr = int(astr)  # 에러발생 : 형변환 불가능함 : int는 unsafe : ok,error 동시 존재 : error의 가능성이 있으면 error핸들링을 해줘야 함

try:        #에러발생 여지가 있으면 넣어준다
    istr = int(astr)
except:     #에러발생시 적용
    istr = -1    

print('Fisrt', istr)

# try 중간 에러 발생 case

astr = 'Bob'

try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1

print('Done', istr)


# Functions : def 명령어 사용해서 생성

x = 1 # variable = name of value
# function = name of code # 이름짓기 : 중요한 개념! : 
def thing():
    print('Hello')

thing() # 함수 호출 : 프로그램은 반복적 코드를 매우 싫어함 -> 추상화함(Abstract) -> 함수생성

# -> print('Hello') 10번 쓰는 것 보다 thing() 10번 쓰는게 나음
# -> 수정점이 적기 때문에! : 추상화(abstration) ! : 함수도 그중 한 방법

# while or for 사용해서 반복 가능
i = 0
while i < 10:
    thing()
    i = i+1

# if loop fuc <- class, Pointer, structure 등 구현 가능 

# 파이썬 펑션 두가지 : 빌트인펑션(기본제공- inpu(),type() 등), 사용자정의펑션

def f(x):   # name of 'parameterized' code : 파라미터에 의해 바뀌는 코드 : x:parameter or formal parameter or formal argument 등으로 부름
    print(x)
    return x # 되돌려 줄 수 있음 --> 변수에 담을 수 있다

f("Hello") # context 1 : context : 함수가 호출되는 지점
f("World") # context 2 : call 호출 argument : 아규먼트 : 실제 콜할때 들어가는 값

y = f("Hello")  # return 값을 받아서 저장
z = f("World")

print(y,z)

big = max('Hello world')    #max 함수로 인해 문자열중 가장 큰 시퀀스 값 선택
print(big)

# To Function or Not To Function : 로지컬한 단위별로 만들면 편하다

# Excercise : 견고한 코딩은 예외처리 필수! Robust하게!
def pay(a, b):
    return a*b + b / 2 *( a - 30 )

# input 함수로 인한 주석 처리
# try:
#     hours = int(input('Enter Hours? : '))
# except:
#     hours = -1

# try:
#     rate = int(input('Enter Rate? : '))
# except:
#     rate = -1

# if hours > 0 and rate > 0:   # 둘다 이상이 없을 경우 출력
#     print("Pay",pay(hours, rate))
# else:
#     print("Not make sense")

# Loop : 반복문 : 무한루프 주의
n = 10

while n  > 0: # 
    print(n)
    n = n - 1

# 무한루프 등 케이스 주의
