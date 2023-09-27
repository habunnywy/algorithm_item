"""
给一个包含n个整数的数组nums，判断nums中是否存在三个元素a,b,c ，使得a+b+c=0，列出所有满足条件且不重复的组合
"""
def three_num(nums:list):
    result = set()
    nums.sort()
    for i in range(len(nums)):
        now_element = nums[i]
        if now_element > 0 :
            continue
        if i != 0 and nums[i] == nums[i-1]:
            continue

        left_index = i+1
        right_index = len(nums)-1
        while left_index<right_index:
            left=nums[left_index]
            right=nums[right_index]
            sum_tmp = now_element+left+right
            if sum_tmp == 0:
                result.add((now_element,left,right))
                left_index += 1
                right_index -= 1
            elif sum_tmp <0:
                left_index += 1
            else:
                right_index -= 1

    return list(result)

nums=[0, 0, 0, 1, 1, 2]
print(three_num(nums))