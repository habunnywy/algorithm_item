 # 读取输入
n,m=map(int,input().strip().split())
cake=[list(map(int,input().strip().split())) for _ in range(n)]

row_sums=[sum(row) for row in cake]
col_sums=[sum(cake[i][j] for i in range(n))for j in range(m)]

if m==1 and n==1:
    print(cake[0][0])
else:
    s1=0
    min_diff_row=float('inf')
    #按行切割
    for i in range(n-1):
        s1 +=row_sums[i]
        s2 = sum(row_sums)-s1
        min_diff_row=min(min_diff_row,abs(s1-s2))

    #按列切割
    s1=0
    min_diff_col=float('inf')
    #按行切割
    for j in range(m-1):
        s1 +=col_sums[j]
        s2 = sum(col_sums)-s1
        min_diff_col=min(min_diff_col,abs(s1-s2))

    print(min(min_diff_row,min_diff_col))