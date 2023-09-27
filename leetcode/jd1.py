# a和b的长度n

n=int(input().strip())
# 接收a
a=input().strip().split()
a=list(map(int,a))


b=[]
b_set=set()

for i in range(n):
    ai=a[i]
    mul=i+1
    # (ai+bi) mod mul==0
    bi_num=0
    while True:
        if ai<mul:
            bi=mul-ai
        else:
            bi=mul-ai%mul
        bi+=mul*bi_num

        if bi not in b_set:
            b.append(bi)
            b_set.add(bi)
            break
        bi_num += 1

print(' '.join(map(str,b)))