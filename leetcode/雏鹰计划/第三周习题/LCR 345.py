from typing import List
'''
345. 反转字符串中的元音字母
简单

给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。
示例 1：

输入：s = "hello"
输出："holle"
示例 2：

输入：s = "leetcode"
输出："leotcede"
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel_list=['A','a','E','e','I','i','O','o','U','u']
        left,right = 0,len(s)-1
        while True:
            while left<right and s[left] not in vowel_list: # 从左向右找元音
                left += 1
            while right>left and s[right] not in vowel_list: # 从右向左找元音
                right -= 1
            if left>=right: # 没找到时，不断增加直到左右指针重合，此时流程结束
                break
            s[left],s[right]=s[right],s[left] # 找到了则进行交换
            left += 1
            right -= 1
        return ''.join(s)

if __name__ == '__main__':
    s = " apG0i4maAs::sA0m4i0Gp0"
    solution = Solution()
    print(solution.reverseVowels(s))