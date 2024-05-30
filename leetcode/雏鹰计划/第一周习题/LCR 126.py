from typing import List
import copy
'''
按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足：

每对相邻的单词之间仅有单个字母不同。
转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。
sk == endWord
给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。
'''
class Node(object):

    def __init__(self,word: str):
        self.word=word
        self.similar_list=[]
        self.routes= []


    def add_similar(self,Node_com):
        self.similar_list.append(Node_com)
        for route in self.routes:
            new_route = copy.deepcopy(route)
            new_route.append(Node_com.word)
            Node_com.routes.append(new_route)

    def find_similar(self,Node):
        for i in range(len(self.word)):
            source_mask = self.word[:i]+'*'+self.word[i+1:]
            target_mask = Node.word[:i]+'*'+Node.word[i+1:]
            if source_mask == target_mask:
                return True
        return False


class WordTree(object):

    def __init__(self,Root):
        Root.routes.append([Root.word])
        self.Root = Root

    def construct_Tree(self, Root_list, Wait_list, end_word):

        while len(Wait_list):
            raw_len=len(Wait_list)
            word_indexs=[_ for _ in range(raw_len)]
            added_num = 0
            end_Node = None
            New_root = []

            for root_node in Root_list:
                for node_index,wait_node in enumerate(Wait_list):
                    if root_node.find_similar(wait_node):
                        if wait_node.word == end_word:
                            end_Node = wait_node
                        root_node.add_similar(wait_node)
                        if node_index in word_indexs:
                            word_indexs.remove(node_index)
                        if wait_node not in New_root:
                            New_root.append(wait_node)
                        added_num += 1

            if end_Node is not None:
                return end_Node.routes
            if added_num == 0:
                return []
            Wait_list = [Wait_list[_] for _ in word_indexs]
            Root_list = New_root

        return []



class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        Root_list = [Node(beginWord)]
        Wait_list = [Node(word) for word in wordList]
        wordTree = WordTree(Root_list[0])
        out = wordTree.construct_Tree(Root_list,Wait_list,endWord)
        return out



if __name__ == '__main__':
    beginWord, endWord, wordList = "hit", "cog", ["hot","dot","dog","lot","log","cog"]
    s = Solution()
    print(s.findLadders(beginWord,endWord,wordList))