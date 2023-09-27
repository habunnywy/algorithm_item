"""
现在有一个只包含数字的字符串，将该字符串转化成IP地址的形式，返回所有可能的情况。
例如：
给出的字符串为"25525522135",
返回["255.255.22.135", "255.255.221.35"]. (顺序没有关系)
"1111"->1.1.1.1

数据范围：字符串长度 0≤n≤12
要求：空间复杂度 O(n!),时间复杂度 O(n!)

注意：ip地址是由四段数字组成的数字序列，格式如 "x.x.x.x"，其中 x 的范围应当是 [0,255]。
"""
s=list(input().strip())
ip_len=len(s)

def is_valid(s):
    len_s=len(s)
    if len_s>1 and s[0]=='0':
        return False
    return int(s)>=0 and int(s)<=255
def main():
    split_index=[max(2,ip_len-6),min(6,ip_len-2)]
    if split_index[0]>split_index[1]:
        return
    out=[]
    for i in range(split_index[0],split_index[1]+1):
        left_ip=s[:i]
        right_ip=s[i:]
        left_split_index=[max(1,len(left_ip)-3),min(3,len(left_ip)-1)]
        right_split_index=[max(1,len(right_ip)-3),min(3,len(right_ip)-1)]
        left_ip_list=[]
        right_ip_list=[]
        for l_i in range(left_split_index[0],left_split_index[1]+1):
            left_ip_1=left_ip[:l_i]
            left_ip_2=left_ip[l_i:]
            if not(is_valid(''.join(left_ip_1)) and is_valid(''.join(left_ip_2))):
                continue
            left_ip_list.append(''.join(left_ip_1)+'.'+''.join(left_ip_2))

        for r_i in range(right_split_index[0],right_split_index[1]+1):
            right_ip_1=right_ip[:r_i]
            right_ip_2=right_ip[r_i:]
            if not(is_valid(''.join(right_ip_1)) and is_valid(''.join(right_ip_2))):
                continue
            right_ip_list.append(''.join(right_ip_1)+'.'+''.join(right_ip_2))

        if len(left_ip_list)==0  or len(right_ip_list)==0:
            continue

        for left in left_ip_list:
            for right in right_ip_list:
                out.append(left+'.'+right)
    print(out)

main()
