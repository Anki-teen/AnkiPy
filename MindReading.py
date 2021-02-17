# 课后练习 读心术
import random
import time

print("读心术...是人类古老而神秘的活动...其原理建立在对图像的感应上\n")
input("按任意键继续\n")
print("如果你有兴趣，不妨抱着虔诚而好奇的心,试试下面图像所带来的读心\n")
input("按任意键继续\n")
print("请你从10到99之间随机取一位自然数，\n用这个自然数依次减去它的个位与十位数，所得数便是你心中结果\n")
input("...")
print("不同的结果一一对应着不同的图案，请找到对应结果数字的图案，请牢牢记住你的图案\n")

num = 1
ran = random.randint(9790,9900)

for i in range(9):
    for j in range(11):
        if num+j in [9,18,27,36,45,54,63,72,81]:
            print("{:>2d}{:<4c}".format(num+j,ran),end="  ")
        else:
            print("{:>2d}{:<4c}".format(num+j,random.randint(9790,9900)),end="  ")
    num += 11
    print("\n")
    
input("用心确认你的图案是否无误,记住它，按任意键继续\n")
scale = 50
print("开始感应你的图案,读心中...".center(scale,"-"))

start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '-' * (scale-i)
    c= (i/scale) * 100
    dur = time.perf_counter() - start
    print("\r{:3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)

print("\n"+"读心结束".center(scale,"-"))
input("按任意键确认图案是否正确")
print("你的图案是\n{:6^c}".format(ran))