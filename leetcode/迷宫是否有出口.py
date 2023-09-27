# 定义四个方向的移动：上、下、左、右
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def can_exit(maze):
    n = len(maze)

    # 初始化访问矩阵
    visited = [[False]*len(row) for row in maze]

    # 深度优先搜索函数
    def dfs(x, y):
        # 当到达最后一行时，表示小人走出了地图
        if x == n - 1:
            return True

        visited[x][y] = True  # 标记当前位置已访问

        # 遍历四个方向
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 检查新位置是否在地图内，是否是墙，以及是否已经访问过
            if 0 <= nx < n and 0 <= ny < len(maze[nx]) and maze[nx][ny] == '0' and not visited[nx][ny]:
                if dfs(nx, ny):
                    return True

        return False

    # 从每一列开始进行搜索
    for y in range(len(maze[0])):
        if maze[0][y] == '0':
            if dfs(0, y):
                return 1

    return -1

maze = [
    "00000111111111",
    "110111101100",
    "00011111000000",
    "110000000111001011",
    "10111111100100",
    "11010101111110000",
    "01010010111110101",
    "10010101011110000",
    "11110000000111011",
    "1101000010100000011111",
    "11111110111101111",
    "01111010110000110000",
]
print(can_exit(maze))  # 输出: 1
