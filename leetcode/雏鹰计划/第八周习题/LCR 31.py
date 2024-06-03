from typing import List
'''
下一个排列
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp_max = 0 # 也可以相邻两两比较
        n = len(nums)
        i = n # 从后往前检
        while i:
            i = i - 1
            # 当前数字比往后所有数字大，表明无法通过后续数字获得更大的字典序
            if nums[i] >= tmp_max:
                tmp_max = nums[i]
                continue
            # 存在往后的某个数字，当前数字恰好小于它，先找到这个数字
            tmp_sorted = sorted(nums[i:],reverse=True) #将当前往后所有进行排序，从大到小是为了解决一个数字出现多次的问题
            now_index = tmp_sorted.index(nums[i]) - 1
            tmp_exactly_value = tmp_sorted[now_index]
            tmp_sorted.pop(now_index)
            nums[i:] = [tmp_exactly_value] + tmp_sorted[::-1]
            break
        else:
            nums[:] = sorted(nums)







if __name__ == '__main__':
    arr = [1,3,2]
    solution = Solution()
    solution.nextPermutation(arr)
    print(arr)

