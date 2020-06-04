class Animal():
    def move(self):
       print ('move')

def move(obj):
    obj.move()

class Dog(Animal):
    def move(self):
        print('Dog move')

class Cat():
    def move(self):
        print('Cat move')

class Porson(Animal):
    pass

if __name__ == '__main__':
    move(Animal())

    d = Dog()
    d.move()

    move(Cat())

    p = Porson()
    p.move()

    move(Porson())

