from typing import List

'''
到最近的人的最大距离

给你一个数组 seats 表示一排座位，其中 seats[i] = 1 代表有人坐在第 i 个座位上，seats[i] = 0 代表座位 i 上是空的（下标从 0 开始）。

至少有一个空座位，且至少有一人已经坐在座位上。

亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。

返回他到离他最近的人的最大距离

输入：seats = [1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 
'''


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        now_zeros_num = 0
        start_index = 0

        while seats[start_index] == 0: # 处理0开头
            start_index += 1
        max_zeros_num = start_index * 2

        for num in seats[start_index:]:
            if not num:
                now_zeros_num += 1
            else:
                if max_zeros_num < now_zeros_num:
                    max_zeros_num = now_zeros_num
                now_zeros_num = 0
        else:
            if seats[-1] == 0: #处理0结尾
                now_zeros_num *= 2
                if now_zeros_num > max_zeros_num:
                    max_zeros_num = now_zeros_num

        return (max_zeros_num + 1) // 2

if __name__ == '__main__':
    s = Solution()
    seats = [0, 0, 1]
    print(s.maxDistToClosest(seats))
