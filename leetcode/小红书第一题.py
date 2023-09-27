# 读入三个整数
first_line=list(map(int,input().strip().split()))
n=first_line[0]
x=first_line[1]
y=first_line[2]

# 读入n天的上班时间列表
work_time=list(map(int,input().strip().split()))
# 读入n天的下班时间列表
off_work_time=list(map(int,input().strip().split()))

value=0
for i in range(n):
    value+=work_time[i]*x
    value=max(0,value-off_work_time[i]*y)
print(value)