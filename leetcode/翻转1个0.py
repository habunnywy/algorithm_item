"""
给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。
示例
输入：[1,0,1,1,0] 输出：4 解释：翻转第一个 0 可以得到最长的连续 1。 当翻转以后，最大连续 1 的个数为 4。
"""

nums_list=[0,0,1,1,0]
def slide_find(nums_list):
    first_zero_index = -1
    second_zero_index = None
    max_one_len = 0
    for i,num in enumerate(nums_list):
        if num == 0:
            now_len = i - first_zero_index - 1
            max_one_len = now_len if now_len > max_one_len else max_one_len
            if second_zero_index != None:
                first_zero_index = second_zero_index
                second_zero_index = i
            else:
                second_zero_index = i

    if nums_list[-1] != 0:
        now_len = len(nums_list) - first_zero_index - 1
        max_one_len = now_len if now_len > max_one_len else max_one_len

    return max_one_len

answer = slide_find(nums_list)
print(answer)