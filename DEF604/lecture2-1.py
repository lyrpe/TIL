# 20200918

# Loop 이 들어가면 어느정도 프로그래밍 가능하다!

# Conditional Steps
# 프로그램은 논리를 표현 ! : Flow Chart 참조
# 플로우차트를 파이썬으로 출력

x = 5

if x < 10:
    print('Smaller') # 꼭 공백 줘야함(보통 4칸) : 파이썬 문법임

if x > 20 :
    print('Bigger')

print('Finis')


# 프로그래밍을 잘한다? : 로직을 명확하게 적을 수 있어야!, 

# Comparison Operators : <, <= ==, >=, >, != 등

x = 5

if x == 5:
    print("Equals 5")

if x < 6: print("Less than 6")  # 한 줄 출력시는 써도 가능 (두문장 이상 안됨)

#같은 스페이스로 묶이면 같은 블럭으로 간주(두칸,세칸,네칸 등 임의로 조절 : 보통 4칸)

print("Before 5")

if x == 5:
    # 같은 스페이스(블럭)으로 묶인 3개 출력
    print("Is 5")
    print("Is Still 5")
    print('Third')

#같은 공백이 아니므로 다른 블럭으로 간주
print('Afterwards 5')

#탭을 공백으로 바꿔주는 에디터를 쓸 것 : 탭은 사용 자제.

#Indentation으로 범위를 정한다! : Scope 라고 사용 함 (C에서 {} 범위)

#Scope는 중첩 될 수 있음 : 포함관계만 가능, 교집합 형식은 불가능

# Nested Decisions 플로우차트 구현
x = 10

if x > 1:
    print('More than one')
    if x < 100 : 
        print('Lss than 100')

print('All Done')

# in C
# x = 10;
# if (x > 1) {
#     printf("More than one");
#     if (x < 100) {
#         print("Less than 100")
#     }
# }

# Two-Way Decisions 플로우차트 구현 : else 활용
x = 4

if x > 2:
    print('Bigger')
else:
    print('Not bigger')

print('All Done')


# Multi-Way : Branch Condition 이 여러개일경우 elif 활용
x = 1

if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('Bigger')

print('All Done')

# No Else
x = 11

if x < 2:
    print('small')
elif x < 10:
    print('Medium')

print('All Done')
