"""
给定正整数n，返回所有和为n的子序列
"""

def sum_combinations(n, current_sum=0, current_combination=[]):
    if current_sum > n:
        return
    if current_sum == n:
        print(current_combination)
        return

    start = 1
    for i in range(start, n - current_sum + 1):
        sum_combinations(n, current_sum + i, current_combination + [i])

# 输出和为3的自然数排列
sum_combinations(3)

#并不单单是 f(n-1)中的每个列表元素+[1] add 额外+[n]，这样仅仅考虑了结尾是1和结尾是n的序列，而没有考虑结尾是2,...,n-1的序列
# 从结尾的可能性去分治考虑是一个很常用的思路
def sum_com(n):
    if n==1:
        return [[1]]
    else:
        out=[]
        for i in range(1,n):
            temp=sum_com(n-i)
            temp_t=[_+[i] for _ in temp]
            out.extend(temp_t)
        out.extend([[n]])
        return out

b=sum_com(4)
print(b)
