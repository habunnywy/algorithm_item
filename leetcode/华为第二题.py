"""
班级组织传球活动，男女同学随机排成 m 行 n 列队伍，第一列中的任意一个男同学都可以作为传球的起点，要求最终将球传到最后一列的任意一个男同学手里，求所有能够完成任务的传球路线中的最优路线（传球次数最少的路线）的传球次数。传球规则：

男同学只能将球传给男同学，不能传给女同学。
球只能传给身边前后左右相邻的同学。
如果游戏不能完成，返回 - 1.
说明：

传球次数最少的路线为最优路线。
最优路线可能不唯一，不同最优路线都为最少传球次数。
输入
班级同学随机排成的 m 行 n 列队伍，1 代表男同学，0 代表女同学。

输入第一行包含两个用空格分开的整数 m(m∈[1,30]) 和 n(n∈[1,30])，表示 m 行 n 列的队伍，接下来是 m 行每行包含 n 个用空格分开的整数 1 或 0。

输出
最优路线的传球次数（最少传球次数）
样例

输入：
4 4
1 1 1 0
1 1 1 0
0 0 1 0
0 1 1 1

输出：
5

提示：
  图一            图二             图三
. . . 0         . . 1 0         1 1 1 0
1 1 . 0         1 . . 0         . . . 0
0 0 . 0         0 0 . 0         0 0 . 0
0 1 . .         0 1 . .         0 1 . .
图一传球路线需要传球6次。
图二传球路线需要传球6次。
图三传球路线需要传球5次，传球次数最少，为最优传球路线。

输入：
3 4
1 0 1 1
1 1 0 0
0 0 1 0

输出：
-1

提示：
选择第1行第1列的男同学作为起点，无法实现按规则将球到最后一列男同学手里。
选择第2行第1列的男同学作为起点，无法实现按规则将球到最后一列男同学手里。

"""

from collections import deque
m,n = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(m)]
# 节点定义:(x,y,pass_lenngth)
def min_passes(matrix):
    queue = deque() # 使用双端队列来执行BFS
    visited = set() # 使用集合来记录节点是否被访问
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    min_lenght = m*n
    def valid_position(x,y):
        return 0<=x<m and 0<=y<n and matrix[x][y]==1
    for i in range(m):
        if matrix[i][0]:
            queue.append((i,0,0)) # 节点状态为(x,y,pass_length)
            visited.add((i,0))
    while queue:
        # 对队列前端节点进行访问并将它所有未被访问的邻接节点放入
        x,y,pass_length = queue.popleft()
        # 判断是否是终点,对于迷宫问题，使用BFS方法，第一个到达终点的必定是最短路径，因此不需要考虑其它未到达终点的
        if y == n-1 :
            return pass_length
        # 如果不是终点，则将所有它的所有未被访问过的邻接节点加入到队列中
        for dx,dy in direction:
            if valid_position(x + dx,y + dy) and (x + dx,y + dy) not in visited:
                queue.append((x + dx,y + dy,pass_length + 1))
                visited.add((x + dx,y + dy))
    return -1
print(min_passes(matrix))