n=int(input())
s=input()
edges=[list(map(int,input().split())) for _ in range(n-1)]

graph={}
#构建连接关系
for edge in edges:
    if edge[0] not in graph:
        graph[edge[0]]=[]
    if edge[1] not in graph:
        graph[edge[1]]=[]
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

def dfs(curr,target,depth,visited):
    if depth==0:
        return 1 if s[curr-1]==target[depth] else 0
    if s[curr-1]!=target[depth]:
        return 0
    visited.add(curr)
    count=0
    for next_node in graph[curr]:
        if next_node not in visited:
            count+=dfs(next_node,target,depth-1,visited)
    visited.remove(curr)
    return count

result=0
for i in range(1,n+1):
    if s[i-1]=='o':
        result+=dfs(i,'oppo',3,set())

print(result)