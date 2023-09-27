
# 递归实现青蛙跳台阶问题
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶，求该青蛙跳上一个n级台阶总共有多少种跳法
# 增加备忘录，避免重复计算
note=dict()
calc_time=0
def dump_num(n):
    global calc_time
    calc_time+=1
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        if (n-1 not in note.keys()) and (n-2 not in note.keys()):
            note[n-1]=dump_num(n-1)
            note[n-2]=dump_num(n-2)
        elif n-1 not in note.keys() and (n-2 in note.keys()):
            note[n-1]=dump_num(n-1)
        elif n-1 in note.keys() and (n-2 not in note.keys()):
            note[n-2]=dump_num(n-2)

        return note[n-1]+note[n-2]

n=10
print(dump_num(n))
print(calc_time)