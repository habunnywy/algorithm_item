"""
题目描述:
    定义f(A)表示将序列 A 进行 unique 操作之后的序列的元素个数。
    unique 操作是指将相邻且相同的元素合成一个元素，再按照原序列的相对顺序进行排列之后得到的序列。例如，[1,1,1,2,2,3,3,1] 进行 unique 操作之后的序列为 [1,2,3,1]；
    [1,2,3,3,2,1] 进行 unique 操作之后的序列为 [1,2,3,2,1]；[1,1,1,1,1] 进行 unique 操作之后得到的序列为 [1]。
    现在，输入一个长度为n的序列S，你需要将其划分为k段，使得每一段都不为空，且你需要最大化所有段的f函数的值之和。你只需要输出这个最大值就行。

输入描述：
    第一行两个正整数n,k(1≤k≤n≤105)；
    第二行n个由空格隔开的正整数a1,a2,...,an(1 ≤ ai ≤10000)，表示输入的序列S。

输出描述：
    输出一个整数，表示所求的最大值。

样例输入：
8 3
1 1 1 2 2 3 3 1

样例输出：
6
"""
from collections import defaultdict
if __name__ == "__main__":
     # 读取第一行的两个正整数n,k
    n, k = map(int, input().strip().split())
    sequence = list(map(int, input().strip().split()))

    last_occurrence = []
    prev_same = [0]*n
    for i in range(n):
        if sequence[i] in last_occurrence:
            prev_same[i] = last_occurrence[sequence[i]] +1
        last_occurrence[sequence[i]] = i

    dp = [[0]*(k+1) for _ in range(n+1)]
    for j in range(1, k+1):
        l=0
        unique_sum = 0
         for i in range(1,n+1):
             while l<i and j

    # ora = 1
    # for i in range(1, n):
    #     if sequence[i] != sequence[i-1]:
    #         ora += 1
    # cuts = 0
    # for i in range(1, n):
    #     if sequence[i] != sequence[i-1]:
    #         cuts += 1
    #
    # result = ora + min(k-1, cuts)
    # print(result)


    # n, k = map(int, input().strip().split())
    # sequence = list(map(int, input().strip().split()))

    # def uni_cnt(sequence):
    #     count = 1 if sequence else 0
    #     for i in range(1, len(sequence)):
    #         if sequence[i] != sequence[i-1]:
    #             count += 1
    #     return count
    #
    # dp = [[0]*(k+1) for _ in range(n+1)]
    # for j in range(1, k+1):
    #     for i in range(1, n+1):
    #         for l in range(i):
    #             dp[i][j] = max(dp[i][j], dp[l][j-1] + uni_cnt(sequence[l:i]))
    #
    # print(dp[n][k])
     # 读取输入的正整