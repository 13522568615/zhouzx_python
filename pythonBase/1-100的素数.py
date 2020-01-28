#打印1-100的素数
sum = 0
for i in range (1, 100):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i)

    #求素数的和
    sum += i
print(sum)