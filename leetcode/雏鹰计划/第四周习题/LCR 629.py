'''
K 个逆序对数组

对于一个整数数组 nums，逆序对是一对满足 0 <= i < j < nums.length 且 nums[i] > nums[j]的整数对 [i, j] 。

给你两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个 逆序对 的不同的数组的个数。由于答案可能很大，只需要返回对 109 + 7 取余的结果。



示例 1：

输入：n = 3, k = 0
输出：1
解释：
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
示例 2：

输入：n = 3, k = 1
输出：2
解释：
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
'''
import time
class Solution:
    def kInversePairs_old(self, n: int, k: int) -> int:
        '''
        这样会超出内存限制
        '''
        mod_num = 10**9 + 7
        if k>n*(n-1)//2:
            return 0
        elif k==0:
            return 1

        if n == 1:
            if k == 0:
                return 1
            else:
                return 0
        if n == 2:
            if k <= 1:
                return 1
            else:
                return 0

        tmp_n = (n-1)*(n-2)
        k = min(k,n*(n-1)//2-k)
        dp=[[0 for _ in range(tmp_n//2+1)] for _ in range(n)]
        dp[0][0],dp[0][1]=1,0
        for i in range(1,n):
            for j in range(tmp_n//2+1):
                if j==0:
                    dp[i][j]=1
                else:
                    tmp_ij=dp[i-1][j]+dp[i][j-1]
                    tmp_ij = max(tmp_ij-dp[i-1][j-i-1],0) if j>i else tmp_ij
                    dp[i][j]=tmp_ij%mod_num
        return dp[-1][k]

    def kInversePairs(self, n: int, k: int) -> int:
        mod_num = 10**9 + 7
        if k>n*(n-1)//2:
            return 0
        elif k==0:
            return 1

        if n == 1:
            if k == 0:
                return 1
            else:
                return 0
        if n == 2:
            if k <= 1:
                return 1
            else:
                return 0

        k = min(k,n*(n-1)//2-k)
        dp1=[0 for _ in range(k+1)]
        dp1[0]=1

        for i in range(1,n):
            dp2=[1]+[0]*k
            for j in range(1,k+1):
                dp2[j]=dp1[j]+dp2[j-1]-(dp1[j-i-1] if j>i else 0)
                dp2[j]%=mod_num
            dp1=dp2

        return dp1[k]

if __name__ == '__main__':
    start_time = time.time()
    s = Solution()
    n,k = 1000,1000
    print(s.kInversePairs(n,k))
    end_time = time.time()
    print(f'time: {end_time-start_time}')