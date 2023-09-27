# 列表长度n
n=int(input().strip())
# 长为n的列表
s=list(map(int,input().strip().split()))
counter={}
for i in s:
    if i in counter:
        counter[i]+=1
    else:
        counter[i]=1

ans=n
for i in range(n):
    target=s[i]
    cnt=0
    cur=0
    j=0
    while j<n:
        if s[j]!=target:
            cnt+=1
            cur=max(cur,j-cnt+1)
            while j-cur>=cur-cnt:
                cur+=1
        j+=1
    ans=min(ans,cur)

print(ans)