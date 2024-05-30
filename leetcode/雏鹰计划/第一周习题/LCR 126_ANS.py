from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ans = []
        if endWord not in wordList:
            return ans
        size = len(beginWord)
        cur_word_set = {beginWord}
        ws = set(wordList)
        # 用于控制bfs结束
        flag = False
        if beginWord in ws:
             ws.remove(beginWord)
        tmp = list('abcdefghijklmnopqrstuvwxyz')
        # key为当前单词，value为能到达该单词（bfs搜索）的单词列表，即该单词的parent
        word_dict = {}
        # bfs
        while cur_word_set:
            # 该次bfs匹配到的单词
            match_set = set()
            for cur in cur_word_set:
                for i in range(size):
                    for j in tmp:
                        if cur[i] == j:
                            continue
                        word = cur[:i] + j + cur[i + 1:]
                        # word在单词列表中
                        if word in ws:
                            # 匹配加入该单词
                            match_set.add(word)
                            # 为该单词维护parent
                            if word not in word_dict:
                                word_dict[word] = []
                            word_dict[word].append(cur)
                            # 到达终点 bfs结束
                            if word == endWord:
                                flag = True
            # 该次bfs结束，剔除掉匹配到的单词
            for el in match_set:
                ws.remove(el)
            # 下次bfs的parent
            cur_word_set = match_set
            if flag: break
        # 完成bfs开始dfs,通过endword反向找parent,直到找到beginword

        # 没有匹到endword,直接结束
        if not flag: return ans
        result = [endWord]
        def dfs(cur_word):
            if cur_word == beginWord:
                ans.append(result[::-1])
                return
            for el in word_dict[cur_word]:
                result.append(el)
                dfs(el)
                result.pop()

        dfs(endWord)
        return ans
