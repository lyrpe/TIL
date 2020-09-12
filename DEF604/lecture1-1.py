###############lecture 1-1######################

# hello world.py
print("*"*10,"Hellow world","*"*10,"\n")

print("Hello World")

print("*"*10,"Hellow world","*"*10,"\n")


# test.py
print("*"*10,"test 1","*"*10,"\n")

x = 1
print(x)
x = x+1
print(x)

print("*"*10,"test 1","*"*10,"\n")

# for문
print("*"*10,"test 2","*"*10,"\n")

for x in range(1,10):
    for y in range(x):
        print("*",end = "")
    print()

print("*"*10,"test 2","*"*10,"\n")


# Constant
print(123) #정수
print(98.6) #소수

print("Hello World")      #싱글/더블 쿼테이션 사용 가능
print('Hello World')      #싱글/더블 쿼테이션 사용 가능

a = 1234
print(a,type(a))    #int형 : type 함수 사용해서 형식 확인 가능

print(type(123))        #int형
print(type("Hello"))    #str형
print(type(98.6))       #float형

print(2**1234)          #제곱형

print(0x1a)             #16진수 표현 : 26
print(10 + 16)

a = 0x1a                #16진수형 자동 저장 가능
print(a)

print(0x1001)           #바이너리 표현
print(bin(30))
print(0b1001)           #바이너리 표현


print(hex(0b1001))      #hex 표현 : 16진수
print(oct(8))           #oct : 8진법

print(50.2)             
print(2.0e12)           #2.0*10^12

# IEEE 754 Standard 기반 실수 표현

#복소수 :complex 형 계산 가능
a = 1+2j
b = 3+4j
print(a+b,type(a+b))
