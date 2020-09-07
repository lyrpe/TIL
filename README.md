# Today I Learned 

# 20200907
class Unit :
    def __init__(self, name, hp, damage):
        self.name = name        #멤버 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력{0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))


## 20191119

### Python

Hello !

* python
* css 3


## 20191119 2
* List
* Plus
