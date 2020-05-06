class MyClass:
    i = 1,2,3,4

    def hello(self):
        return 'hello'

    a = 1
    if a < 0:
        print("负数")
    else:
        if a == 0:
            print("0")
        else:
            print("正数")

x = MyClass()

print(x.a)
print(x.i)
print(x.hello())


