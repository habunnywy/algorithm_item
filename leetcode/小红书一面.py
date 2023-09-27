
def luck_jude(s):
    if len(s)==1:
        return "lucky"
    s_dec=[abs(s[i+1]-s[i]) for i in range(len(s)-1)]
    dec_sort=sorted(s_dec)
    # 检测序列
    i=0
    for n in dec_sort:
        if n==i+1:
            i=n
        else:
            return "Not lucky"
    return "lucky"

import sys
# 读取多行输入
# 读取到结束
for line in sys.stdin.readlines():
    s=line.strip().split()
    s=list(map(int,s))
    n=s[0]
    print(luck_jude(s[1:]))
# s=input().split()
# s=list(map(int,s))
# n=s[0]
# print(luck_jude(s[1:]))
# n=int(input().strip())
# for i in range(n):
#     s=input().strip()
#     s=list(map(int,s))
#     print(luck_jude(s))
