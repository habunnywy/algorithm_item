n,m=map(int,input().strip().split())
matrix=[]
for _ in range(n):
    line=list(map(int,input().strip().split()))
    row=[]
    for i in range(m):
        row.append((line[2*i],line[2*i+1]))
    matrix.append(row)

def reverse(num_tuple):
    return (num_tuple[0],-num_tuple[1])

out_matrix=[]
for j in range(m):
    row=[]
    for i in range(n):
        row.append(reverse(matrix[i][j]))
    out_matrix.append(row)

# 对共轭转置结果进行打印
for i in range(len(out_matrix)):
    for j in range(len(out_matrix[0])):
        print(out_matrix[i][j][0],out_matrix[i][j][1],end=' ')
    print('')