"""
T1 讨厌鬼的数组构造
给定一个长度为 n 的序列啊， 请你构造一个序列b, 序列b满足以下条件：

序列b的长度为n；
对于任意 i ∈ [1, n], 满足
对于任意 i ∈ [1, n], 满足
对于任意
, 满足
输入描述
第一行输入一个整数 n (
)

第二行输入n个整数，第 i 个为

输出描述
输出 n 个整数，表示答案。

若有多个不同的答案，输出任意一个即可。

示例
输入

5 3 4 7 8 10
输出

1 6 2 4 5
"""
# a和b的长度n

n=int(input().strip())
# 接收a
a=input().strip().split()
a=list(map(int,a))


b=[]
b_set=set()

for i in range(n):
    ai=a[i]
    mul=i+1
    # (ai+bi) mod mul==0
    bi_num=0
    while True:
        if ai<mul:
            bi=mul-ai
        else:
            bi=mul-ai%mul
        bi+=mul*bi_num

        if bi not in b_set:
            b.append(bi)
            b_set.add(bi)
            break
        bi_num += 1

print(' '.join(map(str,b)))