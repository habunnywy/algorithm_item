"""
括号配对实质上就是入栈出栈问题，n对括号的可能配对情况是一个卡特兰数

设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

说明：解集不能包含重复的子集。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
from collections import deque
# 解法1：暴力法--遍历生成所有的2^2n括号组合，然后去删除不符合的
def is_valid_match(input_str):
    """
    :param input_str: 输入一个仅由左括号'('和右括号')'构成的字符串
    :return: 若为True则表明这个字符串构成的括号组合是合法的，否则不合法
    """
    stack=[] # 通过检查是否每一个左括号都有一个右括号，且结束时栈是否是空的来判断括号是否合法

    for char in input_str:
        if char=='(':
            stack.append(char)
        elif char==')':
            if not stack:
                return False
            stack.pop()

    return len(stack)==0


def generate_bracket(n):
    """
    遍历生成所有的2^2n括号组合
    :param n: 共有n对括号
    :return: 生成结果
    """
    out = []
    for i in range(2**(2*n)):
        str = bin(i)[2:] # 将左括号视为0，右括号视为1，则所有的可能分别对应于0-2^2n的所有二进制数--多维循环展平,去掉0b
        str = '0'*(2*n-len(str)) + str #补足0
        # 将'0'替换为'(',将'1'替换为')'
        str = str.replace('0','(')
        str = str.replace('1',')')
        out.append(str)
    return out

valid_brackets = list(filter(is_valid_match,generate_bracket(3)))

print(valid_brackets)

# 解法2：通过回溯的方法去生成所有括号组合,递归直到左边
def generate_bracket2(n):
    """

    :param n: n对括号
    :return:返回所有可能的括号结果
    """
    out = []
    def backtrack(S,left,right):
        '''
        回溯的本质就是处理完子序列再根据子序列结果去
        :param S: 用于传递的分支括号列表
        :param left:当前列表的左括号数量
        :param right:当前列表的右括号数量
        :return:None，仅仅当列表长度等于2*n时，添加到out里面
        '''
        if len(S) == 2*n:
            # 括号已经满足到达2n个了
            tmp = ''.join(S)
            out.append(tmp)
        if left < n: # 只要左括号数量未达到n，就可以生长左括号分支
            S.append('(')
            backtrack(S,left+1,right) # 所有子分支的结果
            S.pop() #
        if left > right: # 只有在右括号数量小于左括号，就可以生长右括号分支
            S.append(')')
            backtrack(S,left,right+1)
            S.pop()
    backtrack([],0,0)
    return out

print(generate_bracket2(4))