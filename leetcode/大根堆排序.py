def heap_sort(ary):
    n=len(ary)
    first=int(n/2-1)  #最后一个非叶子节点的索引下标
    for start in range(first,-1,-1):  #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):  #堆排，将大根堆转换成有序数组
        ary[end],ary[0]=ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary


#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root=start
    while True:
        child=root*2+1  #调整节点的子节点
        if child>end: break
        if child+1<=end and ary[child]<ary[child+1]:
            child=child+1  #取较大的子节点
        if ary[root]<ary[child]:  #较大的子节点成为父节点
            ary[root],ary[child]=ary[child],ary[root]  #交换
            root=child
        else:
            break


# 大根堆排序-自写
import math
def my_heapify(arr,start,end):
    # 从start节点到end节点，保证根节点大于子节点
    # 保证从根节点大于子节点
    last_leaf=int(len(arr)/2-1)
    def check(root):
        child=2*root+1
        if child<len(arr)-1 and arr[child]<arr[child+1]:
            child=child+1
        if arr[root]<arr[child]:
            arr[root],arr[child]=arr[child],arr[root]

    for root in range(start,end+1):
        if (2*root+1)>=len(arr):
            return
        else:
            my_heapify(arr,2*root+1,2*root+2)
            check(root)


def creat_heap(arr):
    len_arr=len(arr)
    h=int(math.log2(len_arr+1))+1
    last_leaf=int(len_arr/2-1)
    my_heapify(arr,2**(h-2)-1,last_leaf)
    for i in range(h-3,-1,-1):
        my_heapify(arr,2**i-1,2**(i+1)-1)



def my_heapify2(heap,a=0,top=False):

    if not top:
        i=len(heap)
        heap.append(a)
        while i!=0:
            root=int((i-1)/2)
            if heap[i]>heap[root]:
                heap[i],heap[root]=heap[root],heap[i]
            i=root
    else:
        i=0
        while i<len(heap):
            child=2*i+1
            if child >= len(heap):
                break
            if child<len(heap)-1 and heap[child]<heap[child+1]:
                child+=1
            if heap[i]<heap[child]:
                heap[i],heap[child]=heap[child],heap[i]
            i=child

def my_heapify22(heap,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<len(heap) and heap[largest]<heap[left]:
        largest=left
    if right<len(heap) and heap[largest]<heap[right]:
        largest=right

    if largest!=i:
        heap[i],heap[largest]=heap[largest],heap[i]
        my_heapify22(heap,largest)



def heap_insert(arr):
    """
    插入法去构建大根堆
    """
    heap=[]
    for a in arr:
        my_heapify2(heap,a)
    return heap

def heap_delete(heap):
    arr=[]
    while True:
        arr.append(heap[0])
        if len(heap)==1:
            break
        heap=[heap[-1]]+heap[1:-1]
        my_heapify2(heap,0,top=True)

    return arr

def heap_creat(arr):
    for i in range(len(arr)//2-1,-1,-1):
        my_heapify22(arr,i)



if __name__=='__main__':
    print("堆排序：")
    a=[49,38,65,97,76,13,27,40,99]
    print("排序前：")
    print(a)
    heap_creat(a)
    aa=heap_delete(a)
    print("排序后：")
    print(aa)
