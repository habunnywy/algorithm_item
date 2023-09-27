from collections import deque

m,n=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(m)]
def min_passes(matrix):
    m,n=len(matrix),len(matrix[0])
    direction=[(0,1),(0,-1),(1,0),(-1,0)]

    def is_valid(x,y):
        return 0<=x<m and 0<=y<n and matrix[x][y]==1

    queue=deque() # 用队列进行,把各考虑的节点加入到队列中去
    visited=set()
    for i in range(m):
        if matrix[i][0]==1:
            queue.append((i,0,0)) #x,y,传球次数
            visited.add((i,0))

    while queue:
        x,y,passes=queue.popleft()

        if y==n-1:
            return passes

        for dx,dy in direction:
            new_x,new_y=x+dx,y+dy
            if is_valid(new_x,new_y) and (new_x,new_y) not in visited:
                queue.append((new_x,new_y,passes+1))
                visited.add((new_x,new_y))

    return -1

print(min_passes(matrix))