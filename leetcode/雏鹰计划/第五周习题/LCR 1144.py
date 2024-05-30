from typing import List
'''
递减元素使数组呈锯齿状

给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。

如果符合下列情况之一，则数组 A 就是 锯齿数组：

每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
返回将数组 nums 转换为锯齿数组所需的最小操作次数。

示例 1：

输入：nums = [1,2,3]
输出：2
解释：我们可以把 2 递减到 0，或把 3 递减到 1。
示例 2：

输入：nums = [9,6,1,6,2]
输出：4
'''

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        '''
        奇数去掉第一个值就是偶数的情况了，只要分别做一次真偶数和去掉第一个值后的偶数
        ，随后比较 前者结果 和 后者结果+第一个值减小到比第二个值小的值 的最小值
        '''
        if len(nums)<=2:
            return 0
        def even_min(pos):
            step = 0
            for i,index in enumerate(range(pos+1,len(nums),2)):
                if index == len(nums)-1:
                    min_neighbor = nums[index-1]

                else:
                    min_neighbor = min(nums[index-1],nums[index+1])

                step += max(nums[index]-min_neighbor+1,0)
            return step

        odd_step = max(nums[0]-nums[1]+1,0)
        return min(even_min(0),even_min(1)+odd_step)

if __name__ == '__main__':
    nums = [9,6,1,6,2]
    s = Solution()
    result = s.movesToMakeZigzag(nums)
    print(result)