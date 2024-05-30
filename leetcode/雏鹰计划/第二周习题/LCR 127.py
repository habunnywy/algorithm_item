'''
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：

每一对相邻的单词只差一个字母。
 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
sk == endWord
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。


示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
示例 2：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ans = []
        if endWord not in wordList:
            return 0
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
        if not flag: return 0
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
        return len(ans[0])
