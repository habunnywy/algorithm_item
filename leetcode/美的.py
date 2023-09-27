# 输入列表和元素
input_list=input().strip('[').split(']')
n=int(input_list[-1].strip(','))
if input_list[0]!='':
    input_list=list(map(int,input_list[0].split(',')))
else:
    input_list=[]

def binary_find(input_list,n):
    left=0
    right=len(input_list)-1
    while left<=right:
        mid=(left+right)//2
        if input_list[mid]==n:
            return mid
        elif input_list[mid]<n:
            left=mid+1
        else:
            right=mid-1
    return -1

print(binary_find(input_list,n))