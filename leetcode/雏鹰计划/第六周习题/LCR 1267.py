from typing import List
'''
1267. 统计参与通信的服务器

这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，
1 表示单元格上有服务器，0 表示没有。
如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。
请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。

 
'''

class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        # 为每个服务器生成二维坐标
        server_pos = []
        server_index = 0
        for row,line in enumerate(grid):
            for column,c in enumerate(line):
                if c :
                    server_pos.append((server_index,[row,column]))
                    server_index += 1

        connected_server = set()
        for server_index,pos in server_pos:
            # 行判断
            if sum(grid[pos[0]])>=2:
                connected_server.add(server_index)
                continue
            # 列判断
            if sum(row[pos[1]] for row in grid)>=2:
                connected_server.add(server_index)
                continue

        return len(connected_server)




if __name__ == '__main__':
    solution = Solution()
    grid = [[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]
    print(solution.countServers(grid))