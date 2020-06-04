#逻辑运算
a = 3
b = 4
print(a and b)#当A为3的时候，去运算B，打印的是B得值
print(a or b)#当A为3的时候，为真，直接打印A值
print(not a)#因为A=3所以为假，取反结果
print("----------")
a = 0
b = 4
print(a and b)#因为A等于0为假，所以不会处理到B，打印A得值
print(a or b)#当A为0的时候，为假，直接打印B值
print(not a)#因为A=0所以为真，取反结果
print("----------")
#字符串处理
d = 1
d = str(d)
e = ",xxx"
f = d + e
print(f)

