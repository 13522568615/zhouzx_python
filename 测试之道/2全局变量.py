a = 1
def d():
    global a#global是总体，global+变量的方式引用全局变量
    print(a)#1
    a = 2#引用的全局变量重新赋值为2

if __name__ == "__main__":
    d()
    print(a)#2