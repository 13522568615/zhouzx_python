class TestCss:

    #类属性
    cssa = 'zhangsan'

    #实例方法
    def __init__(self):
        #初始化属性
        self.a = 0
        self.b = 10
        self.color = 'red'

    def info(self):
        print('a:', self.a, 'b:', self.b)

    def Red(self):
        print('color:', self.color)

    #输出类属性
    def CssA(self):
        print('cssa', TestCss.cssa)

if __name__ == '__main__':
    # 实例化TestCss类
    tc = TestCss()
    #在类的内部调用方法
    tc.info()
    tc.Red()
    tc.CssA()

    # 不推荐使用在类外定义属性
    #在类的外部定义以及引用实例属性
    tc.color = 'red'
    print(tc.color)

    #同一个类不同实例，属性是不相同的
    tca = TestCss()
    tca.a = 100
    tca.b = 200
    tca.info()
