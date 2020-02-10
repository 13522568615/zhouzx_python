class A:
    '''
    私有属性
    '''
    def __init__(self):
        #私有属性，只能类自己访问
        self.__ab = 0
        #单下划线开头的变量名是标志性的，子类和类对象都能访问
        self._abc = 0

    def info(self):
        print(self.__ab, self._abc)

a = A()
a.info()

a.__ab = 3#修改属性
a._abc = 3
a.info()#私有属性在外部不能被修改的，所以输出0，单下划线可以访问，所以输出是3

print(a.__ab, a._abc)#输出3.该属性与类内部属性不是互通的
