n,m=map(int,input().strip().split())
# n为货物总数
# m为客户总数
# 读取初始货物排序,对每个字符进行拆分
goods=list(input().strip())
# 读取客户需求
demands=list(input().strip())
# 查找能够满足的客户数量
count=0
for d in demands:
    if d in goods:
        count+=1
        goods.remove(d)
print(count)