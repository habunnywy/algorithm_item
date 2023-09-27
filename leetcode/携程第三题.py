t=int(input())
result=[]
for _ in range(t):
    n,l,r=map(int,input().split())
    arr=list(map(int,input().split()))
    aver_arr=sum(arr)/len(arr)
    if aver_arr<l or aver_arr>r:
        result.append(-1)
        continue
    incre_num,decre_num=0,0
    extra_inc,extra_dec=0,0
    for num in arr:
        if num<l:
            incre_num+=l-num
        elif num>r:
            decre_num+=num-r
        if num<=r:
            extra_inc+=min((r-num),r-l)
        if num>=l:
            extra_dec+=min((num-l),r-l)

    if incre_num>extra_dec or decre_num>extra_inc:
        result.append(-1)
        continue
    if incre_num==decre_num:
        result.append(incre_num)
    elif incre_num>decre_num:
        result.append(incre_num)
    elif incre_num<decre_num:
        result.append(decre_num)

for _ in result:
    print(_)