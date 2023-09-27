"""
问题描述：
给定一个整数序列 S 的长度 n 和一个整数 k。接下来的一行会给出 S 中的 n 个整数。
该问题的目标是将序列 S 分割成 k 个连续的子序列，以使得这 k 个子序列的 "特性值" 之和最大。
这里的 "特性值" 是指子序列中不同的整数的数量。
"""

n, k = map(int, input().strip().split())
S = list(map(int, input().strip().split()))

def f(S):
    unique_S = [S[0]]
    for i in range(1, len(S)):
        if S[i] != S[i - 1]:
            unique_S.append(S[i])
    return len(unique_S)

# dp[i][j]表示前i个元素分成j段的最大值
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        for x in range(i):
            # 不要局限于单一变量变化的思维，既然是二维DP，那么就要考虑两个变量的变化去更新DP
            dp[i][j] = max(dp[i][j], dp[x][j-1] + f(S[x:i])) #遍历去找最大的那一段在哪

print(dp[n][k])
