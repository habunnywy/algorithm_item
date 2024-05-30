from typing import List
"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_section_dict = {}
        max_section_len = 0
        for num in nums:
            if num not in nums_section_dict:
                num_left_len = nums_section_dict.get(num-1,0)
                num_right_len = nums_section_dict.get(num+1,0)
                cur_num_len = num_left_len + num_right_len + 1
                if cur_num_len>max_section_len:
                    max_section_len = cur_num_len

                nums_section_dict[num] = cur_num_len
                if num_left_len!=0:
                    nums_section_dict[num-num_left_len] = cur_num_len
                if num_right_len!=0:
                    nums_section_dict[num+num_right_len] = cur_num_len
        return max_section_len

if __name__ == '__main__':
    s = Solution()
    nums = [0,3,7,2,5,8,4,6,0,1]
    out = s.longestConsecutive(nums)
    print(out)