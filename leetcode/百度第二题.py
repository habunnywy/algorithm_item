"""
3 2
1 9 3
2 7 8
7

小明的公司要进行集体活动，活动要求所有人员分组。
当前有n个人，每个人的能力值为ai,性格值为bi,现在希望将这n个人分成若干组，
每个人只能在一个组内。当然，分组是一个问题，
我们定义两个人的差别值为能力值的差和性格值的差之和，即|ai-aj|+|bi-bj|。
 在分组前，我们规定一个差别上限L，如果两个人的差别值不超过L，
 那么在分组结果中这两个人一定会在同一组内(当然，即使两个人差别值超过L，
两个人还是可以在同一个小组内，只是不超过L的必须在一组)。
现在我们想知道，如果能将所有人分成至少k个非空的小组，规定的差别上限L最多为多少。
 输入描述： 第一行两个正整数n,k，表示人数和分组要求。 接下来两行每行n个整数，表示a1,a2,...,an和b1,b2,...,bn
 输出描述 输出一个整数表示最多的差别上限L 样例输入：
 3 2
 1 9 3
 2 7 8
 样例输出： 7
 样例解释： 1和2的差别值为9-7+7-2=13 2和3的差别值为9-3+8-7=7 1和3的差别值为3-1+8-2=8， 故
 差别值上限为7时，2和3必须在一组，1单独一组，此时有2组。 二上限为8时，2和3必须一组，1和3必须一组，
 所以1，2，3只能一起一组，此时只有1组，不满足要求，故差别值上限为7.
"""

n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))




# 得用并查集
parent=[0]*n

differences=[]
for i in range(n):
    for j in range(i+1,n):
        diff=abs(a[i]-a[j])+abs(b[i]-b[j])
        differences.append(diff)
differences.sort()
left,right=0,len(differences)-1
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    rootx=find(x)
    rooty=find(y)
    if rootx!=rooty:
        parent[rooty]=rootx

def check(mid):
    for i in range(n):
        parent[i]=i
    for i in range(n):
        for j in range(i+1,n):
            if abs(a[i]-a[j])+abs(b[i]-b[j])<=mid:
                union(i,j)
    groups=set()
    for i in range(n):
        groups.add(find(i))

    return len(groups)<= k

answer=-1
while left!=right:
    mid=(left+right)//2
    if not check(differences[mid]):
        left=mid+1
    else:
        answer=differences[mid]
        right=mid-1
print(differences[right])