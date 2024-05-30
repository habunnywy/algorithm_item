'''
191. 位1的个数
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中
设置位
的个数（也被称为汉明重量）。

 示例 1：

输入：n = 11
输出：3
解释：输入的二进制串 1011 中，共有 3 个设置位。
示例 2：

输入：n = 128
输出：1
解释：输入的二进制串 10000000 中，共有 1 个设置位。
示例 3：

输入：n = 2147483645
输出：30
解释：输入的二进制串 11111111111111111111111111111101 中，共有 30 个设置位。

'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bin = list(bin(n)[2:])
        n_bin = map(int,n_bin)
        return sum(n_bin)

if __name__ == '__main__':
    n = 2147483645

    solution = Solution()
    print(solution.hammingWeight(n))