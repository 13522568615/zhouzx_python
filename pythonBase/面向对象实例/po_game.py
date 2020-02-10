#面向过程编程
"""
虫子的初始位置
蚂蚁的初始位置
进入循环，条件为蚂蚁和虫子不再同一个位置
依照规则，蚂蚁和虫子移动位置
直到蚂蚁和虫子走到同一位置，程序结束
"""
import random

#蚂蚁
ant_point = random.randint(0,20)
#虫子
worm_point = random.randint(0,20)
#输出虫子与蚂蚁的初始位置
print("蚂蚁：", ant_point, "虫子：", worm_point)
#指定可以走的步数
step = [-2, +2, -3 ,+3]

#进入循环
while ant_point != worm_point:
    #选择步数
    astep = random.choice(step)
    #判断蚂蚁走的步数是否超出了范围
    if 0 <= ant_point + astep <=20:
        #不超出范围从新修改位置
        ant_point += astep
    # 选择步数
    astep = random.choice(step)
    #判断虫子走的步数是否超出了范围
    if 0 <= worm_point +astep <= 20:
        # 不超出范围从新修改位置
        worm_point += astep
    #输出虫子与蚂蚁现有位置
    print("蚂蚁：", ant_point, "虫子：", worm_point)

