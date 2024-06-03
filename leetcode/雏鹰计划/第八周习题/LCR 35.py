from typing import List
'''
85. 最大矩形
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
'''

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 获得每个元素为右下角时的最大矩形，需要收集行方向和列方向
        m, n = len(matrix), len(matrix[0])

        # 统计每行从左到右连续的1的个数，收集行的信息
        left_1 = [[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left_1[i][j] = left_1[i][j - 1] + 1 if j > 0 else 1

        # 行收集完了，收集列，即高度多1。每多一列，要构成矩形，宽度是最短的那一行
        '''    
        例：
        001111 -> h=1, s = h*w = 1*4
        
        000111
        001111 -> h=2, s = h*w = 2 * min(4,3) = 6
        
        000001
        000111
        001111 -> h=3, s = h*w = 3 * min(4,3,1) = 3 
        '''

        max_area = 0
        for i in range(m):
            for j in range(n):
                if not left_1[i][j]:
                    continue
                k = i
                while k >= 0 and left_1[k][j]:
                    height = i - k + 1
                    width = min([row[j] for row in left_1[k:i+1]])
                    max_area = max(max_area, height * width)
                    k = k - 1

        return max_area



class Solution2:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        left = [0] * n  # Initialize left as the number of consecutive '1's ending at each column
        max_area = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] += 1
                else:
                    left[j] = 0

            # Use the histogram method to find the largest rectangle for this row
            max_area = max(max_area, self.largestRectangleArea(left))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)  # Append a zero to make sure we empty the stack at the end

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        heights.pop()  # Remove the zero that we appended

        return max_area


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    solution = Solution()
    print(solution.maximalRectangle(matrix))