N = 5       #商品的种类
W = 11      #背包的承重
w = [0,1,2,5,6,7]    #商品的承重，不使用 w[0]
v = [0,1,6,18,22,28]   #商品的价值，不使用 v[0]

dp=[[0]*(W+1)]*(N+1) #dp[i][j]表示前i个物品放入容量为j的背包的最大价值

for i in range(1,N+1):
    for j in range(1,W+1):
        if j-w[i]>=0:
            dp[i][j]=max(dp[i-1][j-w[i]]+v[i],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[N][W])
