"""
题目描述:
给定一个经过编码的字符串，返回它解码后的字符串。编码规则为: k[encoded string]，表示其中方括号内部的 encoded string 正好重复 k 次。注意 k 保证为正整数。
输入描述:
输入经过编码的字符串。你可以认为输入字符串总是有效的，输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或214]的输入。
注意:可多层嵌套，例如例如2[b3[d]] 对应的输出为 bdddbddd
输出描述:
输出对应的解码字符串
样例输入:
3[a]2[bc]
样例输出:
aaabcbc
提示
利用栈进行操作
"""


class Solution:
    def code_str(self,input_str,index=0):

        need_copy_number = 0
        need_str = ''
        while index<len(input_str):
            char = input_str[index]
            if char.isdigit():
                need_copy_number = need_copy_number*10 + int(char)
            elif char == '[':
                tmp_str,index = self.code_str(input_str,index = index+1)
                need_str += need_copy_number*tmp_str
            elif char == ']': #碰到字符
                return need_str,index
            else:
                need_str += char
            index += 1
        return need_str,index # 没碰到[]


    def decodeString(self,input_str: str) -> str:
        return self.code_str(input_str)[0]

test_str = 's3[a]'
s = Solution()
out = s.decodeString(test_str)
print(out)



