#测试数据组数T
T=int(input())

out=[]

def find_max(n,h1,hn):
    global bridge_max
    global bridge_min
    if n<=2:
        if abs(h1-hn)<=1:
            now_max=max(h1,hn)
            bridge_max=max(bridge_max,now_max)
            return
        else:
            bridge_min=-1
            return
    if (n-1)<abs(h1-hn):
        bridge_min=-1
        return
    else:
        mid=min(h1+(n-1)//2,hn+(n-1)//2)
        bridge_max=max(bridge_max,mid)
        if n%2==0:
            find_max(n//2,h1,mid)
            find_max(n//2,mid+1,hn)
        else:
            find_max(n//2+1,h1,mid)
            find_max(n//2+1,mid,hn)

for _ in range(T):
    # 读取桥柱的个数n,第一根和最后一根桥柱的高度h1,hn
    bridge_max = 0
    bridge_min = 0
    n,h1,hn=map(int,input().strip().split())
    find_max(n,h1,hn)
    if bridge_min==-1:
        out.append(-1)
    else:
        out.append(bridge_max)

for i in out:
    print(i)