
# Break문
# Continue문
# input 함수로 인한 주석 처리
# While 문 : Indefinite loop : 몇번 실행될지 미리 결정되어 있지 않다
# while True:
#     line = input('> ')
#     if line = ""
#         continue
#     if line[0] == '#':    # 값 미입력시 [0]에 값이 없어서 에러 발생함 : leng(line) >= 1 처리 해줘야 함
#         continue    # 처음 시작으로 돌려보냄
#     if line == 'done':
#         break       # 빠져나감
#     print(eval(line)) # 계산 기능 적용
#     print(line)

# for : definite loop : 미리 몇번 돌지가 결정되어 있는 루프
# for i in [5, 4, 3, 2, 1]: # 리스트도 가능
# for i in ["A", "b","c"]: # 리스트도 가능
for i in range(1,10): # i = 1.... 10-1
    print("Hello",i)

print("Done!")

# Excercise : 가장 큰 값 출력 함수 
import random

def largest(lst):
    m = None ## 의미 없는 값  : None
    # m = lst[0]
    for i in lst:
        if m == None or i > m:
            m = i

        # if i > m:
        #     m = i
    return m
    #return max(lst)

def smallest(lst):
    m = None ## 의미 없는 값  : None

    for i in lst:
        if m == None or i < m:
            m = i
    return m

def count(lst):
    r = 0
    for i in lst:
        r = r+1
    return r

def sum(lst):
    r = 0
    for i in lst:
        r = r + i
    return r

def average(lst):
    return sum(lst) / count(lst)

def count_even(lst): #짝수 개수 세기
    r = 0
    for i in lst:
        if i % 2 == 0:
            r = r + 1
    return r

def find(lst, x):
    # found = False
    for i in lst:
        if i == x:  # is = (==) 임, is/is not 오퍼레이터도 지원 함 
            return True
    return False


# data generation
lst = []
#for i in range(0, 10):
for i in range(0,random.randint(5,20)):
    lst.append (random.randint(1, 100000))

# print statistics : 통계치 출력 : very simple data analysis!
print(lst)
print("largest  : " , largest(lst))
print("smallest : " , smallest(lst))
print("Count : " , count(lst))
print("count_even : " , count_even(lst))
print('#Odd : ', count(lst)- count_even(lst))
print("Sum : " , sum(lst))
print("Average : " , average(lst))
print("Find 3? : ", find(lst,3))
print("Find " + str(lst[0]) + "?" , find(lst,lst[0]))
