"""


给定一个只包含左右括号的合法括号序列，按右括号从左到右的顺序输出每一对配对的括号出现的位置（括号序列以0开始编号)。

输入描述:
仅一行，表示一个合法的括号序列。 长度不超过100000。


输出描述:
设括号序列有n个右括号。则输出包括n行，每行两个整数l，r，表示配对的括号左括号出现在第l位，右括号出现在第r位。

示例
输入:
(())()
输出:
1 2
0 3
4 5
"""
# 使用一个堆栈存储左括号下标，堆栈碰到左括号则将下标入栈，碰到右括号则出栈
from collections import deque
def bracket_match(str):
    out = []
    left_bracket_index_stack = deque() # 使用双向列表模拟堆栈
    for i,s in enumerate(str):
        if s == '(':
            left_bracket_index_stack.append(i)
        elif s == ')':
            out.append((left_bracket_index_stack.pop(),i))
    return out

out = bracket_match(input())
for _,__ in out:
    print(_,__)