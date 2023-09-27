from collections import defaultdict
import math
#检查一个数是否是完全平方数
def is_square(num):
    return int(math.sqrt(num))**2==num
#DFS遍历，染红符合条件的节点
def dfs(node,parent):
    global red_nodes
    for neighbor in tree[node]:
        if neighbor ==parent:
            continue
        dfs(neighbor,node)
        if is_square(weights[node]*weights[neighbor] )and not visited[node] and not visited[neighbor]:
            red_nodes+=2
            visited[node]=True
            visited[neighbor] = True

n=int(input().strip())
weights=list(map(int,input().strip().split()))

tree=defaultdict(list)
for _ in range(n-1):
    u,v=map(int,input().strip().split())
    tree[u-1].append(v-1)
    tree[v- 1].append(u - 1)

visited=[False]*n
red_nodes=0
dfs(0,-1)
print(red_nodes)

