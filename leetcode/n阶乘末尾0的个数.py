"""
递归求解n阶乘末尾0的个数
"""
n = 5
num2 = 0
num5 = 0
if n <2:
    print(0)
else:
    for i in range(2,n+1):
        if i%2 == 0:
            num2 += 1
        if i%5 == 0:
            num5 += 1
    print(min(num2,num5))