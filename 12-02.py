class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "파랑"
myCar2.Speed = 0

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재속도는 %dkm입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차1의 색상은 %s이며, 현재속도는 %dkm입니다." % (myCar1.color, myCar1.speed))


myCar3.upSpeed(0)
print("자동차1의 색상은 %s이며, 현재속도는 %dkm입니다." % (myCar1.color, myCar1.speed))



