# 输入订单数量n
n=int(input())
# n个订单的下单时刻,s是排序完毕的
s=list(map(int,input().split()))
# n个订单的往返时间
t=list(map(int,input().split()))
# n个订单的酬劳
a=list(map(int,input().split()))
# DP问题
dp=[0]*n # dp[i]表示以第i个订单为最后一个订单时的最大酬劳
dp[0]=a[0]
max_a=a[0]
for i in range(1,n):
    # 考虑第i个订单是否可以作为最后一个订单
    for j in range(i):
        if s[i]>=(s[j]+t[j]):
            dp[i]=max(dp[i],dp[j]+a[i])

    dp[i]=max(dp[i],a[i])# 单独作为最后一个订单
    max_a=max(max_a,dp[i])
print(max_a)