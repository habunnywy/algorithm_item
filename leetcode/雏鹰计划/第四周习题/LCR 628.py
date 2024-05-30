'''
628. 三个数的最大乘积
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。


示例 1：

输入：nums = [1,2,3]
输出：6
示例 2：

输入：nums = [1,2,3,4]
输出：24
示例 3：

输入：nums = [-1,-2,-3]
输出：-6
'''
from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        nums = sorted(nums)
        positive_len = 0
        for _ in nums[::-1]:
            if _>0:
                positive_len += 1
            else:
                break
        if not positive_len: #全是负数，则三数结果必定为负数，返回最后三数乘积
            return nums[-1]*nums[-2]*nums[-3]
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1]) # 比较三正 和 一正两负谁大

if __name__ == '__main__':
    s = Solution()
    nums = [-100,-2,-3,1]
    print(s.maximumProduct(nums))