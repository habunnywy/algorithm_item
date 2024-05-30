from typing import List
'''
给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        self.data = [[0 for _ in range(n)] for __ in range(n)]

        def set_column(column_index,row_start_index,start_value_list,is_reverse=False):
            if is_reverse:
                start_value_list = start_value_list[::-1]
            for value in start_value_list:
                self.data[row_start_index][column_index] = value
                row_start_index += 1

        def set_row(row_index,column_start_index,start_value_list,is_reverse=False):
            if is_reverse:
                start_value_list = start_value_list[::-1]
            for value in start_value_list:
                self.data[row_index][column_start_index] = value
                column_start_index += 1

        def set_screw(n, start_fit_index, start_value_list):
            if n == 1:
                self.data[start_fit_index][start_fit_index] = start_value_list[0]
                return
            if n == 2:
                self.data[start_fit_index][start_fit_index] = start_value_list[0]
                self.data[start_fit_index][start_fit_index+1] = start_value_list[1]
                self.data[start_fit_index+1][start_fit_index+1] = start_value_list[2]
                self.data[start_fit_index+1][start_fit_index] = start_value_list[3]
                return

            set_row(row_index=start_fit_index,column_start_index=start_fit_index,start_value_list=start_value_list[:n-1])
            set_column(column_index=start_fit_index+n-1,row_start_index=start_fit_index,start_value_list=start_value_list[n-1:2*n-2])
            set_row(row_index=start_fit_index+n-1, column_start_index=start_fit_index+1, start_value_list=start_value_list[2*n-2:3*n-3],
                    is_reverse=True)
            set_column(column_index=start_fit_index,row_start_index=start_fit_index+1,start_value_list=start_value_list[3*n-3:4*n-4],
                       is_reverse=True)
            set_screw(n-2, start_fit_index=start_fit_index+1, start_value_list=start_value_list[4*n-4:])

        start_value_list = [_ for _ in range(1,n*n+1)]

        set_screw(n,start_fit_index=0,start_value_list=start_value_list)

        return self.data

    def generateMatrix2(self, n: int) -> List[List[int]]:

        self.data = [[0 for _ in range(n)] for __ in range(n)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)] # 定义四个方向
        x,y,dir_index = 0,0,0 # 定义初始x,y位置，初始方向
        for i in range(1,n*n+1):
            self.data[x][y] = i
            dx,dy = dirs[dir_index]
            x_temp,y_temp = x+dx,y+dy # 预计前往的下一步
            # 判断下一步是否已经超出边缘，或者已经填充过
            if x_temp<0 or y_temp<0 or x_temp>=n or y_temp>=n or self.data[x_temp][y_temp]>0:
                # 已经超出边缘了，则变换方向，并重新提取下一步
                dir_index = (dir_index + 1) % 4
                dx,dy = dirs[dir_index]
            x,y = x+dx,y+dy #真正的下一步
        return self.data

if  __name__=='__main__':
    n = 5
    s = Solution()
    print(s.generateMatrix2(n))