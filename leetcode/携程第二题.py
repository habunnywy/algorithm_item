n,m=map(int,input().strip().split())
matrix=[]
for _ in range(n):
    input_str=list(input())
    matrix.append(input_str)
count=0
str_set=['y','o','u']
# 第一种三角形
for i in range(n):
    for j in range(m):
        first_point=matrix[i][j] #遍历第一个定点
        if first_point not in str_set:
            continue
        for k in range(i+1,n):
            second_point=matrix[k][j]
            if second_point not in str_set or second_point == first_point:
                continue
            for l in range(j+1,m):
                third_point=matrix[k][l]
                if third_point not in str_set or third_point in [first_point,second_point]:
                    continue
                count+=1

for i in range(n):
    for j in range(m):
        first_point=matrix[i][j] #遍历第一个定点
        if first_point not in str_set:
            continue
        for k in range(i+1,n):
            second_point=matrix[k][j]
            if second_point not in str_set or second_point == first_point:
                continue
            for l in range(j-1,-1,-1):
                third_point=matrix[k][l]
                if third_point not in str_set or third_point in [first_point,second_point]:
                    continue
                count+=1

for i in range(n):
    for j in range(m):
        first_point=matrix[i][j] #遍历第一个定点
        if first_point not in str_set:
            continue
        for k in range(j-1,-1,-1):
            second_point=matrix[i][k]
            if second_point not in str_set or second_point == first_point:
                continue
            for l in range(i+1,n):
                third_point=matrix[l][k]
                if third_point not in str_set or third_point in [first_point,second_point]:
                    continue
                count+=1

for i in range(n):
    for j in range(m):
        first_point=matrix[i][j] #遍历第一个定点
        if first_point not in str_set:
            continue
        for k in range(j+1,m):
            second_point=matrix[i][k]
            if second_point not in str_set or second_point == first_point:
                continue
            for l in range(i+1,n):
                third_point=matrix[l][k]
                if third_point not in str_set or third_point in [first_point,second_point]:
                    continue
                count+=1

print(count)