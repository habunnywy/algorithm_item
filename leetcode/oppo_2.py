# 接收矩阵函数
"""
4
1011
1101
0101
1010
out:16
"""
n= int(input().strip())

# 读取矩阵,均为01组成，且中间没有空格
matrix=[]
for _ in range(n):
    line=input().strip()
    row=[]
    for c in line:
        row.append(int(c))
    matrix.append(row)
# 可视化距离矩阵
matrix_distance=0

def get_v_distance(i,j):
    v_dis=0
    if matrix[i][j]==1:
        if i>0:
            for k in range(i-1,-1,-1):
                if matrix[k][j]==1:
                    v_dis+=1
                if matrix[k][j]==0:
                    break
        if i<n-1:
            for k in range(i+1,n):
                if matrix[k][j]==1:
                    v_dis+=1
                if matrix[k][j]==0:
                    break
    else:
        if i>0:
            for k in range(i-1,-1,-1):
                if matrix[k][j]==0:
                    v_dis+=1
                if matrix[k][j]==1:
                    break
        if i<n-1:
            for k in range(i+1,n):
                if matrix[k][j]==0:
                    v_dis+=1
                if matrix[k][j]==1:
                    break

    return v_dis

def get_h_distance(i,j):
    h_dis=0
    if matrix[i][j]==1:
        if j>0:
            for k in range(j-1,-1,-1):
                if matrix[i][k]==1:
                    h_dis+=1
                if matrix[i][k]==0:
                    break
        if j<n-1:
            for k in range(j+1,n):
                if matrix[i][k]==1:
                    h_dis+=1
                if matrix[i][k]==0:
                    break
    else:
        if j>0:
            for k in range(j-1,-1,-1):
                if matrix[i][k]==0:
                    h_dis+=1
                if matrix[i][k]==1:
                    break
        if j<n-1:
            for k in range(j+1,n):
                if matrix[i][k]==0:
                    h_dis+=1
                if matrix[i][k]==1:
                    break
    return h_dis

matrix_v_distance=[[] for _ in range(n)]
matrix_h_distance=[[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i>0:
            if matrix[i-1][j]==matrix[i][j]:
                h_dis=matrix_h_distance[i-1][j]
            else:
                h_dis = get_h_distance(i, j)
        else:
            h_dis = get_h_distance(i, j)

        if j>0:
            if matrix[i][j-1]==matrix[i][j]:
                v_dis=matrix_v_distance[i][j-1]
            else:
                v_dis=get_v_distance(i,j)
        else:
            v_dis=get_v_distance(i,j)
        d=v_dis+h_dis
        matrix_distance+=d
        matrix_h_distance[i].append(h_dis)
        matrix_v_distance[i].append(v_dis)

print(matrix_distance)