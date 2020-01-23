class Complex:
    def __init__(self, age ,name):
        self.age = age
        self.name = name

x = Complex(10,'zhangsan')
print(x.age, x.name)