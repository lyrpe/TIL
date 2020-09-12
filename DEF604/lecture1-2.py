###############lecture 1-2######################
# String
a = "Hello"
a                       #문자열 그대로 표현
print(a, type(a))       #print사용시 a내 문자열 표현

a = 'I said "Hello"'    #따옴표 사용위해 싱글쿼테이션 사용
print(a)

a = "i said 'Hello'"    #더블쿼테이션도 가능
print(a)

a= "i said \"Hello\""           #이스케이프 백슬러쉬 사용 : 스페셜 문자 출력시 사용
print(a)

print("\n")             #New Line
a = "Line1 \n Line2"
print(a)

a = "\\"
print(a)

a = """
a
b
c
d
e
f
"""                    # """ : 라인브레이크 상태로 Define : 긴 문장 정의 시 용이 함
print(a)

# Boolean : 참/거짓
a = 1
b = 2
print(a == b , type(a==b))

# 0 : Fale, 0이 아닌수 : True
c = (a==b)
print(c, type(c))

d = (a != b)        # 다른지 비교 : True
print(d, type(d))

# 변수 : 메모리 주소 할당하여 셀에 저장
a = 2 ** 128    # a변수에 값 저장 : 메모리 내 저장
print(2 ** 128)

x = 12.2        # 변수는 할당된 메모리 셀에 저장  -> 메모리 주소 할당 -> 변수 연계
y = 14

x = 100         # 변수값 변경 가능(overwrite)

# 변수명 Rule 
# : 숫자시작 변수 사용 불가, #/. 등 특수 기호 사용 불가, 대문자는 가능
# Reserved Word : 예약어는 변수로 사용 할 수 없음 : False, Class, return, is, finally 등
# : 의미있는 변수명 사용 ex) 
hours = 35
rate = 12.50
pay = hours * rate

print(pay)

# 구성단위 : Sentences or Line
x = 2       # Assignment
x = x+2     # Assignment with expression : 대입문, 오퍼레이터(연산자)
print(x)    # Print Statement : 펑션

# Equal Sign(=) 활용   (variable) 변수 = expression (right-hand sid)
x = 0.6                 # 좌측/우측에 오는 메모리주소 자체를 참조하여 업데이트
x = 3.9 * x * (1-x)     # x라는 Memory Location 에 우측의 expression 을 저장하라
print(x)

# 변수 삭제 : Deleting Variables
a = 1
print(a, type(a))

del a                   # a삭제 : 
#print(a, type(a))       # name 'a' is not defined
