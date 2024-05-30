"""
小美拿到了一个字符串s，她准备按以下的规则生成一个字符串t
1,首先令t等于s。
2.若s不为空，删除s最后一个字符，然后将剩下的字符加入t的后缀。
3.若不为空，删除s第一个字符，然后将剩下的字符加入t的后缀。
4.若s不为空，回到第二步，否则结束。
操作结束后，小美有若干次询问，每次查询t的第x个字符是多少。
输入描述:
第一行输入两个正整数n,q，n代表字符串s的度，以及询问次数。第二行输入一个长度为n的、仅由小写字母组成的字符串，代表字符串s。
接下来的q行，每行输入一个正整数t，代表一次查询1 ≤ n,q < 10^5,1<an*(n+1)/2
输出描述:
输出q行，每行输出一个小写字母代表查询的答案
"""
# 第k段的开始和结束下标  k*(2*n-k+1)/2  --- (k+1)*(2*n-k)
n,q = map(int,input().split())
s = input()
str_index_list = [(k,int( k*(2*n-k+1)/2) ) for k in range(n)]
out = []
def find_k_segment(quires):
    for i in range(n):
        if i == n-1:
            return str_index_list[i]
        if str_index_list[i][1] <= quires <= str_index_list[i+1][1]:
            return str_index_list[i]
while q:
    q -= 1
    quires = int(input()) - 1
    # 查询quires对应那一个片段
    segment_k,segment_k_start_index = find_k_segment(quires)
    shift_index = quires - segment_k_start_index
    need_add_index = segment_k//2 # 因删除而需要补充的开头下标
    out.append(s[shift_index + need_add_index])

for _ in out:
    print(_)