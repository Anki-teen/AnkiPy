#水仙花数
for i in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

#正整数反转
num = int(input("num=\n"))
revernum = 0
while num > 0:
    revernum = num * 10 + num % 10
    num //= 10
print(revernum)

#百钱百鸡
for x in range(21):
    for y in range(34):
        z = 100 - x - y
        if 5*x +3*y+z ==100 and z % 3 == 0:
            prinr(f"公鸡{x}只，母鸡{y} 小鸡{z}")

#斐波那契数列
a,b = 1,1
for i in range(18):
    a,b = b,a+b
    print(1,1,b,end=" ")

#打印素数
for num in range(2,100):
    prime = True
    for factor in range(2,num-1):
        prime = False
        break
    if prime == True:
        print(num)

#多元一次方程组正整数解

