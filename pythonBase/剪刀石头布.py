"""
剪刀石头布
"""
#导入随机模块
import random

#玩家
user = int(input("剪刀输入0，石头输入1，布输入2。请输入："))
#电脑--固定输入石头1
# computer = 1
#电脑--随机数字
computer = random.randint(0, 2)
print("电脑输入：" + str(computer))

if (int((user == 0)and(computer == 1))or((user == 1)and(computer == 2))
        or((user == 2)and(computer == 0))):
    print("玩家获胜")

elif user == computer:
    print("平局")

else:
    print("电脑获胜")