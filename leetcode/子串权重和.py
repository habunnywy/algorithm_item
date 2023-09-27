
"""
小美定义一个 01 串的权值为：每次操作选择一位取反，使得相邻字符都不相等的最小操作次数。
例如，"10001"的权值是 1，因为只需要修改一次：对第三个字符取反即可。
现在小美拿到了一个 01 串，她希望你求出所有非空连续子串的权值之和，你能帮帮她吗？
"""
def weight(s):
    s_temp=s.copy()
    cnt=0
    if len(s)==2:
        return 1 if s_temp[0]==s_temp[1] else 0

    for i in range(1,len(s_temp)-1):
        if s_temp[i-1]==s_temp[i]:
            if s_temp[i]!=s_temp[i+1]:
                cnt+=1
                s_temp[i-1]=0 if s_temp[i]==1 else 1
            else:
                cnt+=1
                s_temp[i]=0 if s_temp[i-1]==1 else 1
        elif s_temp[i-1]!=s_temp[i]:
            if s_temp[i]!=s_temp[i+1]:
                continue
            else:
                cnt+=1
                s_temp[i+1]=0 if s_temp[i]==1 else 1
    return cnt


def solve(string):
    n=len(string)
    total_weight=0

    for l in range(2,n+1):  # l 是子串的长度
        for i in range(0,n-l+1):  # i 是子串的起始位置
            substring=string[i:i+l]
            total_weight+=weight(substring)

    return total_weight


if __name__=='__main__':
    string=input().strip()
    string=[int(s) for s in string]
    print(solve(string))
