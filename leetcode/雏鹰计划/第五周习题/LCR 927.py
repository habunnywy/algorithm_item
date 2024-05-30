from typing import List
'''
给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。

如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：

arr[0], arr[1], ..., arr[i] 为第一部分；
arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
这三个部分所表示的二进制值相等。
如果无法做到，就返回 [-1, -1]。

注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。

示例 1：

输入：arr = [1,0,1,0,1]
输出：[0,3]
示例 2：

输入：arr = [1,1,0,1,1]
输出：[-1,-1]
示例 3:

输入：arr = [1,1,0,0,1]
输出：[0,2]

'''
import time
class Solution:
    def threeEqualParts1(self, arr: List[int]) -> List[int]:
        '''
        暴力方法--超时
        '''
        if not arr.count(1) % 3:
            return [-1,-1]

        n = len(arr)
        def listToint(arr):
            return int(''.join(str(x) for x in arr)) # 这里是一个生成式表达式

        for i in range(n):
            for j in range(i+2,n):
                part1 = listToint(arr[:i+1])
                part2 = listToint(arr[i+1:j])
                part3 = listToint(arr[j:])
                if part1 == part2 and part2 == part3:
                    return [i,j]

        return [-1,-1]

    def threeEqualParts2(self, arr: List[int]) -> List[int]:
        '''
        做了部分减枝，时间复杂度O(n^2),还是超时
        '''
        def remove_leading_zeros(arr):
            i = 0
            while i < len(arr) and arr[i] == 0:
                i += 1
            return arr[i:]

        ones_index = [index for index,value in enumerate(arr) if value == 1]
        ones_counts = len(ones_index)
        if ones_counts % 3:
            return [-1,-1]
        if ones_counts == 0:
            return [0,len(arr)-1]
        # 计算每部分应该有多少个1
        one_part_num = ones_counts//3
        i_start,i_end = ones_index[one_part_num-1],ones_index[one_part_num]
        j_start,j_end = ones_index[one_part_num*2-1],ones_index[one_part_num*2]
        for i in range(i_start,i_end):
            for j in range(j_start,j_end):
                part1 = remove_leading_zeros(arr[:i+1])
                part2 = remove_leading_zeros(arr[i+1:j+1])
                part3 = remove_leading_zeros(arr[j+1:])
                if part1 == part2 and part2 == part3:
                    return [i,j+1]
        return [-1,-1]

    def threeEqualParts(self, arr: List[int]) -> List[int]:
        '''
        时间复杂度优先
        :param arr:
        :return:
        '''
        ones_index = [index for index, value in enumerate(arr) if value == 1]
        ones_counts = len(ones_index)

        if ones_counts % 3 != 0:
            return [-1, -1]

        if ones_counts == 0:
            return [0, len(arr) - 1]

        one_part_num = ones_counts // 3

        # 找到分割点
        first = ones_index[0] # 第一个部分 1开始的地方
        second = ones_index[one_part_num] # 第二个部分 1开始的地方
        third = ones_index[2 * one_part_num] # 第三个部分 1开始的地方

        # 可见，第三部分是固定的！！！因此，第二部分第一个1往后的和第三部分后续应该一模一样
        # 三个部分，从切分的1开始，就应该一样
        length = len(arr) - third

        if arr[first:first + length] == arr[second:second + length] == arr[third:]:
            return [first + length - 1, second + length]

        return [-1, -1]

    def threeEqualParts(self, arr: List[int]) -> List[int]:
        '''
        空间复杂度优先
        '''
        ones_counts = sum(arr)

        if ones_counts % 3 != 0:
            return [-1, -1]

        if ones_counts == 0:
            return [0, len(arr) - 1]

        one_part_num = ones_counts // 3
        first = second = third = 0
        tmp_num = -1
        for i,c in enumerate(arr):
            if c == 1:
                tmp_num += 1
                if tmp_num == 0:
                    first = i
                elif tmp_num == one_part_num:
                    second = i
                elif tmp_num == one_part_num*2:
                    third = i

        # 可见，第三部分是固定的！！！因此，第二部分第一个1往后的和第三部分后续应该一模一样
        # 三个部分，从切分的1开始，就应该一样
        length = len(arr) - third

        if arr[first:first + length] == arr[second:second + length] == arr[third:]:
            return [first + length - 1, second + length]

        return [-1, -1]

if __name__ == '__main__':
    start_time = time.time()
    arr = [1,0,1,0,1]
    solution = Solution()
    print(solution.threeEqualParts(arr))
    end_time = time.time()
    print(end_time-start_time)