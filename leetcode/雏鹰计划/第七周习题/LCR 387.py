
'''
387. 字符串中的第一个唯一字符

给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1.

示例 1：
输入: s = "leetcode"
输出: 0

示例 2:
输入: s = "loveleetcode"
输出: 2
示例 3:

输入: s = "aabb"
输出: -1
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_list = []
        delete_dict = {chr(i): False for i in range(ord('a'), ord('z') + 1)}
        char_order = dict()
        for i,c in enumerate(s):
            if c in char_list:
                char_list.remove(c)
                delete_dict[c] = True
            elif not delete_dict[c]:
                char_list.append(c)
                char_order[c] = i
        if len(char_list)==0:
            return -1
        return char_order[char_list[0]]

    def firstUniqChar2(self, s: str) -> int:
        char_list = []
        delete_dict = {chr(i): False for i in range(ord('a'), ord('z') + 1)}
        char_order = dict()
        for i,c in enumerate(s):
            if c in char_list:
                char_list.remove(c)
                delete_dict[c] = True
            elif not delete_dict[c]:
                char_list.append(c)
                char_order[c] = i
        if len(char_list)==0:
            return -1
        return char_order[char_list[0]]



if __name__ == '__main__':
    s = 'aadadaad'
    solution = Solution()
    print(solution.firstUniqChar(s))
