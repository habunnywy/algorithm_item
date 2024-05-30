from typing import List
from collections import defaultdict
'''
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]
'''


# class Node(object):
#     letter_list = 'abcdefghijklmnopqrstuvwxyz'
#     def __init__(self, data):
#         self.data = data
#         self.parent = self
#         self.rank = 0
#
#     def str_equal(self,s_com):
#         if set(self.data)!=set(s_com):
#             return False
#         for l in Node.letter_list:
#             if self.data.count(l)!=s_com.count(l):
#                 return False
#         return True
#
#     def find(self):
#         now_root = self
#         while now_root != now_root.parent:
#             now_root = now_root.parent
#         return now_root
#
#     def merge(self, other):
#         self_parent = self.find()
#         other_parent = other.find()
#         if self_parent == other_parent:
#             return
#         if self_parent.rank < other_parent.rank:
#             self_parent.parent = other_parent
#         elif self_parent.rank > other_parent.rank:
#             other_parent.parent = self_parent
#         else:
#             other_parent.parent = self_parent
#             self_parent.rank += 1

class Solution:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for s in strs:
            s_trans = ''.join(sorted(s))
            str_dict[s_trans].append(s)

        return list(str_dict.values())

if __name__ == '__main__':
    s = Solution()
    str1 = ["eat","tea","tan","ate","nat","bat"]
    print(s.groupAnagrams(str1))