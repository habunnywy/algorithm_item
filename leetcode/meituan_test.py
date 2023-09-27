import sys

"""
3
1 2 2
2 3
out:2
"""


# 读取站的数量
n=sys.stdin.readline().strip()
# 站之间的距离
arr=sys.stdin.readline().strip().split()
arr=[int(i) for i in arr]

# 读取出发地和目的地
line=sys.stdin.readline().strip().split()
m,n=int(line[0]),int(line[1])
m=m-1
n=n-1

# 出发地和目的地顺时针和逆时针距离计算
sun_distance=0
ni_distance=0
if m<n:
    sun_distance=sum(arr[m:n])
    ni_distance=sum(arr[:m])+sum(arr[n:])
else:
    sun_distance=sum(arr[n:m])
    ni_distance=sum(arr[:n])+sum(arr[m:])

print(min(sun_distance,ni_distance))

