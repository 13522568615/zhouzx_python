class user:
    def eat(self):
        print("吃")

class Animal(user):
    def eat(self):
        print("吃饭")

#子类调用重写方法
u = Animal()
u.eat()

#子类对象调用父类方法
super(Animal,u).eat()
