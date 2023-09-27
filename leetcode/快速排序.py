
def swap_num(arr,index_a,index_b):
    arr[index_a],arr[index_b] = arr[index_b],arr[index_a]


def quick_sort(arr):
    if len(arr)==2:
        return [arr[0],arr[1]] if arr[0]<=arr[1] else [arr[1],arr[0]]
    elif len(arr)<=1:
        return arr
    else:
        left_move_done=False
        right_move_done=False
        # 指针移动
        p=arr[-1]
        # 把标定点值从arr中取出
        arr=arr[:-1]
        left_p=0
        right_p=len(arr)-1
        while True:
            # 左指针移动
            while arr[left_p]<=p :
                left_p+=1
                if left_p==len(arr):
                    left_move_done=True
                    break
            if left_move_done:
                out=quick_sort(arr)
                out.append(p)
                return out

            # 右指针移动
            while arr[right_p]>=p and right_p>left_p:
                right_p-=1
                if right_p==-1:
                    right_move_done=True
                    break
            if right_move_done:
                out=quick_sort(arr)
                out.insert(0,p)
                return out

            # 左右指针重合
            if left_p==right_p:
                out_left=quick_sort(arr[:left_p])
                out_right=quick_sort(arr[left_p:])
                out_left.extend([p])
                out_left.extend(out_right)
                return out_left

            # 交换
            swap_num(arr,left_p,right_p)

def quick_sort_gpt4(arr):
    if len(arr)<=1:
        return arr

    pivot=arr[-1]
    left,right=[],[]
    equal_num=0
    for i in arr[:-1]:
        if i<pivot:
            left.append(i)
        elif i>pivot:
            right.append(i)
        else:
            equal_num+=1

    return quick_sort(left)+[pivot]*equal_num+quick_sort(right)

def quick_sort_gpt4_partition(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_gpt4_partition(arr, low, pivot_index)
        quick_sort_gpt4_partition(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high


    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] > pivot and right >= left:
            right -= 1

        if right < left: # 左右指针重合时退出
            break
        else: # 交换
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


arr = [3,2,1,8,6,7,7,5,5,5]
out=quick_sort_gpt4(arr)
print(out)  # Output will be [1, 1, 2, 3, 6, 8, 10]

