###############lecture 1-3######################
#Expression

#Numeric Expressions
# Operator 
xx = 2
xx = xx +2
print(xx)

yy = 440 * 12
print(yy)

zz  = yy / 1000     #인티져 나눗셈은 //로 사용
print(zz)
print(10//3)

#Order of Evaluation : 곱셉/나눗셈, Power, 괄호 등 우선순위 일반적인 내용 사용
#Operator Precedence : 상동

# Type 의미
# 파이썬은 Dynamic Type 부여 But, 타입은 통일해서 계산해야 됨
# 1 + "Str" : 불가
# 1 + Ture : 자동변환 가능

ddd = 1+4
print(ddd,type(ddd))

eee= 'Hello' + ' there'     #이어 붙이기 가능 : 양쪽이 str 경우
print(eee,type(eee))

# eee = eee +1 : can only concatenate str (not "int") to str : 타입에러 발생

xx = 1  
print(type(xx))        #int
temp = 98.6
print(type(temp))      #float

# Type Conversion

# 형변환 가능
print(float(99)+100)
print(int(float(99)+100))

a= 1+2.0  # 기본적으로 int->float로 변환

#integer Division : 파이썬3 버전에서는 나눗기 결과가 int여도 float로 변환
print(10/2)
print(9/2)


sval = str(123)
print(sval,type(sval))

sval = int(sval) #형변환
sval = sval + 1
print(sval,type(sval))  #변환 후 계산 가능

#User Input
# nam = input('Who are you')  # 출력과 입력값 요청 -> nam에 입력값 저장

# ex ) 유럽형 층 계산 -> 미국형 층 계산
inp = input('Europe Floor?')   # exception 처리 원래는 해줘야 함
usf = int(inp)+1
print('Us floor', usf)


# Comment
x = 1 # This is comment. C에서는 //

# 사람이 이해 할 수 있는 프로그램인가? : 다른사람이 쉽게 접근하고 사용할 수 있는 코드가 좋은 프로그램!

# Chapter1 Summary


