"""
一个N位的正整数，如果把它的各个位数重新排列，则可以得到一些新的N位正整数。如果原数在所用重排得到的新数中降序排列第K个，则称原数的SXF序数是K。
例如一个四位数7225，将它各个数位重排，得到7522 7252 7225 5722 5272 5227 ...，其中7225排在第三位，故7225的SXF序数是3
现在给定一个正整数a，请计算它的SFX序数
输入描述： 第一行是一个正整数T，表示接下来又T组测试数据 加下来是各组的测试数据，每行一个正整数
输出描述： 对于每组测试数据输出一行，仅有一个整数，表示其SFX序数
例子： 输入： 5 7225 65421 123 1024 365895456 输出： 3 1 6 18 28149
"""
import math
from collections import Counter
def sfx_seq(num):
    num_str=str(num)
    sorted_num_str=sorted(num_str)
    rank=0
    n=len(num_str)
    counter=Counter(sorted_num_str)
    for i,digit in enumerate(num_str):
        for smaller_digit in sorted(set(sorted_num_str)):
            if smaller_digit>=digit:
                break
            rank+=counter[smaller_digit]*math.factorial(n-i-1)
        counter[digit]-=1
        if counter[digit]==0:
            sorted_num_str.remove(digit)

    return rank+1

T=int(input())
out=[]
for _ in range(T):
    a=int(input())
    out.append(sfx_seq(a))
for _ in range(len(out)):
    print(out[_])
