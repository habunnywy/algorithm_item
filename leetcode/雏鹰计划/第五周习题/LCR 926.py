from typing import List
'''
如果一个二进制字符串，是以一些 0（可能没有 0）
后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。
给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。
返回使 s 单调递增的最小翻转次数。

示例 1：

输入：s = "00110"
输出：1
解释：翻转最后一位得到 00111.
示例 2：

输入：s = "010110"
输出：2
解释：翻转得到 011111，或者是 000111。
示例 3：

输入：s = "00011000"
输出：2
解释：翻转得到 00000000。

'''

class Solution:

    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        forward_filp_nums = [0] * (n+1) #append涉及动态增加内存，这样费时间，如果已经知道结果长度，使用预设更好
        # backward_filp_nums = [0] #第pos后面的0个数不用统计的，
        # 因为后面0的个数=总数-1总数-pos前面0总数=总数-1总数-(pos-pos前面0总数)

        for pos in range(n):
            forward_filp_nums[pos+1] = forward_filp_nums[pos] + (s[pos] == '1')

        min_flip_nums = n

        for i in range(n+1):
            flips = forward_filp_nums[i] + n - forward_filp_nums[-1] - \
                    (i - forward_filp_nums[i])
            min_flip_nums = flips if flips < min_flip_nums else min_flip_nums

        return min_flip_nums

    def minFlipsMonoIncr2(self, s: str) -> int:
        n = len(s)
        prefix_ones = [0] * (n + 1)


        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + (s[i] == '1')

        min_flips = float('inf')

        for i in range(n + 1):
            flips = prefix_ones[i] + (n - i - (prefix_ones[n] - prefix_ones[i]))
            min_flips = min(min_flips, flips)

        return min_flips

    def minFlipsMonoIncr3(self, s: str) -> int:
        '''
        使用动态规划，对每个可行的翻转结果的每个位置考虑
        考虑每个位置是0还是1的前缀最小翻转次数。
        dp[i][0] = dp[i-1][0] + (s[i]=='1')
        dp[i][1] = min(dp[i-1][0],dp[i-1][1]) + (s[i]=='0')
        '''
        dp0,dp1 = 0,0
        for c in s:
            dp1 = min(dp0,dp1)
            if c == '1':
                dp0 += 1
            else:
                dp1 += 1
        return min(dp0,dp1)

if __name__ == '__main__':
    solution = Solution()
    s = '010110'
    print(solution.minFlipsMonoIncr(s))