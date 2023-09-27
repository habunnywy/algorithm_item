# 读取花架数量n
n=int(input().strip())
# 接下来n行，每行四个整数，分别表示第i个画架上四个颜色的价格（红、白、黄、粉）
# 读取n行
floor_matrix=[]
for i in range(n):
    s=input().strip().split()
    s=list(map(int,s))
    floor_matrix.append(s)

# 对矩阵进行转置
floor_matrix=list(map(list,zip(*floor_matrix)))
# 小程需要花光的钱
from collections import defaultdict
sum_dict=defaultdict(list)
for i,mi in enumerate(floor_matrix[0]):
    for j,mj in enumerate(floor_matrix[1]):
        sum_dict[mi+mj].append([i+1,j+1])

money=1000
count=0
for k,mk in enumerate(floor_matrix[2]):
    for l,ml in enumerate(floor_matrix[3]):
        comple=money-mk-ml
        if comple in sum_dict:
            for i,j in sum_dict[comple]:
                count+=1
print(count)