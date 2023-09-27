# 输入的nums大小
n=int(input().strip())
# 输入所有保温长度
s=list(map(int,input().strip().split()))
# 需要重发的报文
sn=int(input().strip())
def is_sorted(lst):
    before=lst[:-1]
    after=lst[1:]
    sorted_value=True
    unsorted_index=-1
    for i in range(n-1):
        if before[i]>after[i]:
            sorted_value=False
            unsorted_index=i+1
            return sorted_value,unsorted_index
    return sorted_value,unsorted_index
sorted_value,unsorted_index=is_sorted(s)
if sorted_value:
    try:
        start=s.index(sn)
    except Exception:
        start=-1
    s.reverse()
    try:
        end=n-s.index(sn)-1
    except Exception:
        end=-1
    print(start,end)
else:
    try:
        start=s[unsorted_index:].index(sn)+unsorted_index
    except Exception:
        try:
            start=s[:unsorted_index].index(sn)
        except Exception:
            start=-1
    try:
        tmp=s[:unsorted_index]
        tmp.reverse()
        end=unsorted_index-tmp.index(sn)-1
    except Exception:
        try:
            tmp=s[unsorted_index:]
            tmp.reverse()
            end=len(tmp)-tmp.index(sn)-1+unsorted_index
        except Exception:
            end=-1

    print(start,end)