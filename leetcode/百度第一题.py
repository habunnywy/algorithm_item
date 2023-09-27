"""
给定一个长度为n的序列a1,a2,...,an,你可以删去其中最多n-1个数，
得到一个新序列b1,b2,...,bm(删除后不可改变原来的相对顺序)。
现在希望删去某些数后使得新序列的第i个数的值恰好为i，即bi=i
想知道最少需要删去多少个数可以使得新序列满足条件。如果如何都不能做到，请输出-1
输入描述： 第一行一个正整数n，表示序列长度 接下来一行n个空格隔开的数字a1,a2,...,an
输出描述 输出一个整数表示最少需要删去的个数，如果做不到，输出-1
样例输入： 5 1 4 2 3 5
样例输出： 2
解析：对1 4 2 3 5删去4和5后得到序列1 2 3正好满足条件
"""
n=int(input().strip())
arr=list(map(int,input().strip().split()))

count=1
match_num=0
for num in arr:
    if num==count:
        match_num+=1
        count+=1

print(n-match_num if match_num>0 else -1)