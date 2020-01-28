#打印1-100的素数
sum = 0
count = 0
for i in range (1, 100):
    suShu = True#suShu等于真
    for j in range(2, i):
        if i%j == 0:
            suShu = False
            break
    #每输出5次换行
    if suShu:#如果suShu是真的话
        print(i,end=" ")#输出i，并且空格
        count += 1#count自加1
        if (count%5 == 0):#如果count等于5时，5%5==0时
            print("\n")#换行

    #求素数的和
    sum += i
print(sum, end="\n")