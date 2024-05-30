from typing import List
from collections import defaultdict
'''
347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。


示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]


提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的


进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
'''
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        统计结束后，进行排序
        '''
        num_times_dict = defaultdict(int)
        for num in nums:
            num_times_dict[num] += 1
        num_sorted = sorted(num_times_dict,key=lambda key:num_times_dict[key],reverse=True)
        return num_sorted[:k]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        '''
        桶排序，使用频率作为数组下标
        '''
        num_times_dict = defaultdict(int)
        freq_list = [[]for _ in range(len(nums)+1)]
        for num in nums:
            num_times_dict[num] += 1
        for key,value in num_times_dict.items():
            freq_list[value].append(key)

        preK_num = []
        temp_k = 0
        freq_index = 1
        while temp_k<k and freq_index<=len(nums):
            if freq_list[-freq_index] == []:
                freq_index+=1
                continue
            tmp_list = freq_list[-freq_index]
            preK_num.extend(tmp_list)
            temp_k += len(tmp_list)
            freq_index += 1
        return preK_num

if __name__ == '__main__':
    s = Solution()
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    out = s.topKFrequent2(nums,k)
    print(out)