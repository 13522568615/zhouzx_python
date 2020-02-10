# 面向对象编程（面向对象分析）
'''
游戏中的对象有：地图/虫子/蚂蚁
地图是一维的，只需要记录虫子和蚂蚁的位置
蚂蚁和楚公子知道自己的位置
蚂蚁和虫子能按照规则移动
定义地图，蚂蚁，虫子三个类
主程序中实例化它们，并通过对象间的交互；来完成游戏的模拟
'''

import random

class Sprite:
    """
    精灵类
    """
    # 行走的步数
    step = [-2, +2, -3, +3]

    def __init__(self, gm, point=None):
        # gm为地图实例
        self.gm = gm
        # 如果point=None
        if point is None:
            # 那么精灵会初始化位置
            self.point = random.randint(0, 20)
        else:
            self.point = point

    # 步数方法
    def jump(self):
        # 选择步数
        astep = random.choice(Sprite.step)
        # 判断蚂蚁走的步数是否超出了范围
        if 0 <= self.point + astep <= 20:
            # 不超出范围从新修改位置
            self.point += astep


# 蚂蚁继承父类
class Ant(Sprite):
    # 构造方法
    def __init__(self, gm, point=None):
        # 子类方法中调用父类方法
        super().__init__(gm, point)
        # 添加设置蚂蚁在地图当中的位置
        self.gm.set_point('ant', self.point)

    # 重写父类方法
    def jump(self):
        # 调用父类方法
        super().jump()
        # 添加设置蚂蚁在地图当中的位置
        self.gm.set_point('ant', self.point)


# 虫子类
class Worm(Sprite):
    # 构造方法
    def __init__(self, gm, point=None):
        # 子类方法中调用父类方法
        super().__init__(gm, point)
        # 添加设置蚂蚁在地图当中的位置
        self.gm.set_point('worm', self.point)

    # 重写父类方法
    def jump(self):
        # 调用父类方法
        super().jump()
        # 添加设置蚂蚁在地图当中的位置
        self.gm.set_point('worm', self.point)


# 地图类
class GameMap:
    def __init__(self):
        # 记录蚂蚁和虫子的位置
        self.ant_point = None
        self.worm_point = None

    # 判断蚂蚁和虫子相遇的方法
    def catched(self):
        print('ant:', self.ant_point, 'worm:', self.worm_point)
        # 游戏结束的条件
        if self.ant_point is not None and self.worm_point is not None and self.ant_point:
            return True

    def set_point(self, src, point):
        if src == 'ant':
            self.ant_point = point
        if src == 'worm':
            self.worm_point = point


if __name__ == '__main__':
    # 实例化地图类
    gm = GameMap()
    # 实例化虫子类，并且在地图上标记自己的位置
    worm = Worm(gm)
    # 实例化蚂蚁类，并且在地图上标记自己的位置
    ant = Ant(gm)
    # 如果在地图上蚂蚁没有遇到虫子，那么就一直循环，否则退出循环
    while not gm.catched():
        worm.jump()
        ant.jump()
