import sys


input_line=0
tian_num=0
tian_list=[]

for line in sys.stdin:
    input_line+=1
    a = line.split()
    if input_line==1:
        tian_num=int(a[0])
    if input_line==2:
        for num in a:
            tian_list.append(int(num))
        break

nozero_tian_num=0
sum_tian=0
for i in tian_list:
    sum_tian+=i
    if i!=0:
        nozero_tian_num+=1

if tian_num>=sum_tian:
    print('-1')
else:
    print("{}".format(nozero_tian_num+1))

