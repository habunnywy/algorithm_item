

def edit_distance(true_s,out_s):
    m=len(true_s)
    n=len(out_s)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif true_s[i-1]==out_s[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    i,j=m,n
    insert_error,delete_error,subs_error=0,0,0
    while i>0 and j>0:
        if i>0 and j>0 and true_s[i-1]!=out_s[j-1]:
            if dp[i][j]==1+dp[i-1][j-1]:
                subs_error+=1
                i,j=i-1,j-1
                continue
        if i>0 and dp[i][j]==1+dp[i-1][j]:
            delete_error+=1
            i-=1
        elif j>0 and dp[i][j]==1+dp[i][j-1]:
            insert_error+=1
            j-=1
        else:
            i,j=i-1,j-1
    return insert_error,delete_error,subs_error

true_s=input().strip()
out_s=input().strip()
insert_error,delete_error,subs_error=edit_distance(true_s,out_s)
print(insert_error)
print(delete_error)
print(subs_error)