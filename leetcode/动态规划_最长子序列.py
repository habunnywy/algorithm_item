"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
"""
"""
原l长的问题拆分为最后一个元素是否是最长严格递增子序列的
"""
nums=[99,100,101,102,3,4,5] #索引值-1即可
n=len(nums)
dp=[1]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for j in range(1,i):
        if nums[j-1]<nums[i-1]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))


"""
# 采用贪心+二分查找的方法，降低时间复杂度到nlogn
贪心：最长序列应该增长得尽量慢。通过维持一个数组d[i],表示长度为i的最长上升子序列最小元素。
通过遍历nums[j]，如果nums[j]>d[len]，说明nums[j]可以直接加在所有原子序列后面，因此扩增d。
而若 存在k st. d[k]<nums[j]<d[k+1]，说明nums[j]可用于更新i长度的最小值，从而降低增长速度。
而由于数组d[i]的单调性，二分查找可用于寻找k,时间复杂度为logn

原因：虽然将 d[k+1]更新为 nums[i] 不会影响 当前最长升序子序列（同时也不会影响已经判断过的升序子序列的长度），
但是将 d[k+1]更新为 nums[i] 是有意义的，因为在 nums[i] 之后的序列中，还会有更多的数字，
且刚好可以和 d[1,...,k] + nums[i] +其他数字凑成最长升序子序列。
这一步的意义，在于记录最小序列，代表了一种“最可能性”
"""
def binary_search(sorted_list,a):
    len_list=len(sorted_list)
    compare_index=len_list//2
    if len(sorted_list)==0:
        return 0
    elif len(sorted_list)==1:
        if sorted_list[0]>a:
            return 0
        else:
            return 1
    if sorted_list[compare_index]==a or \
            sorted_list[compare_index]>a and sorted_list[compare_index-1]<a:
        return compare_index
    elif sorted_list[compare_index]>a:\
        return binary_search(sorted_list[:compare_index],a)
    else:
        return len_list//2+binary_search(sorted_list[compare_index:],a)

if __name__=='__main__':
    d=[]
    for m in nums:
        index=binary_search(d,m)
        if index!=len(d):
            d[index]=m
        else:
            d.append(m)
    print(len(d))