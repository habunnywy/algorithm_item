#接收字符长度
n=int(input().strip())

# 要扩增的字符
s_start='o'
s_op='ppo'
# 可扩增的倍数
k=(n-1)//len(s_op)
# 余数
r=(n-1)%len(s_op)
# 扩增后的字符
s_op=s_op*k
s_op+=s_op[:r]
s_op=s_start+s_op
if n>=4:
    print(s_op)
else:
    temp='oppo'
    print(temp[:n])