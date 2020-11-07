import math 

def nums():
    numls = []
    num = input("Please input your number.\
            \nENTER to quit ")
    while num != "":
        numls.append(num)
        num = input("Please input your number.\
            \nENTER to quit ")
    return numls

def dealfor(numls):
    f = input("Please input your formula\n")
    f=f.replace("^","**")
    length = len(numls)
    for i in range(length):
        a = chr(97+i)
        f=f.replace(a,numls[i])
    f=f.replace("e","math.e")
    f=f.replace("log","math.log")
    f=f.replace("sqrt","math.sqrt")
    return f

while 1:
	numls = nums()
	formula = dealfor(numls)
	print(eval(formula))
	a=input("end")
