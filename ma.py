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

# 组合公式

def fac(num):
    result = 1
    for n in range(num+1):
        result *= n
    return result

m = int(input("m = "))
n = int(input("n = "))
prin(fac(m) // fac(n) // fac(m-n))

# 三数求和

def add(a=0,b=0,c=0):
    return a+b+c

print(add(c=50,a=100,b=200))
"""带默认值参数需放在非默认值参数后面"""

# 多数求和

def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add(4,5,6)+add(1,2))

"""可变参数"""
































