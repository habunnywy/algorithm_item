# 读取矩阵阶数n
n=int(input().strip())
matrix=[]
# 读取矩阵
for i in range(n):
    matrix.append(list(map(float,input().strip().split())))
# 读取初始v
v_old=list(map(float,input().strip().split()))
# 对v进行归一化
v_old=[v_old[i]/sum(v_old) for i in range(n)]
v=v_old
# 使用公式v=matrix*v更新v 10000次
mult_sum=1
while True:
    v_old = v
    v=[sum([matrix[j][k]*v_old[k] for k in range(n)]) for j in range(n)]
    #对v进行范数归一化,因为前面一次迭代已经归一化了，因此这次的模长接近于比例因子
    sum_square=sum([v[i]**2 for i in range(n)])**0.5
    if abs(sum_square-mult_sum) <= 0.001:
        break
    mult_sum=sum_square
    v=[v[i]/sum_square for i in range(n)]

# 调试
v_div=[v[i]/v_old[i] for i in range(n)]
# 对mult_sum保留两位小数输出
print('%.2f'%mult_sum)