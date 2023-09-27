"""
题目描述：
在一些大学里，学生发表论文的话会有一定的奖学金加分。另外，对于一篇论文，其作者的顺序不同，加分也不相同。
在本题中，一篇论文最多仅三个作者，其中第一作者加 3 分，第二作者加 2 分，第三作者加 1 分。
在这一年，学校一共有n篇论文发表。你需要输出按照字典序从小到大输出每一名作者以及其对应的加分总数是多少。

输入描述：
第一行输入一个正整数n(1≤n≤100)，表示论文数量。
接下来n行，每一行第一个数字表示该篇论文的作者数，之后输入对应个数的仅由小写英文字母组成的字符串，
每两个字符串用空格隔开。分别表示这一篇论文的第一作者，第二作者，......的名字。每一个作者的名字长度不超过 20。
每一篇论文最多三个作者，且这三个作者名字都不同。

输出描述
按照字典序从小到大输出每个作者的名字以及其对应的加分总数，中间用空格隔开。每一个作者的信息单独输出一行。

样例输入
4
3 george annie jack
2 jack peter
2 peter bakh
1 zack

样例输出
annie 2
bakh 2
george 3
jack 4
peter 5
zack 3
"""
import sys
from collections import defaultdict
if __name__ == "__main__":
     # 读取第一行的n
    n = int(input().strip())
    author_scores = defaultdict(int)
    # 读取n行的论文输入，其中每一行的第一个为该篇论文的作者数，之后输入对应个数的仅由小写英文字母组成的字符串，每两个字符串用空格隔开，如 3 george annie jack
    for _ in range(n):
        paper_info = input().strip().split()
        author_count = int(paper_info[0])

        for i in range(author_count):
            author = paper_info[i+1]
            if i ==0 :
                author_scores[author] += 3
            elif i==1:
                author_scores[author] += 2
            elif i == 2:
                author_scores[author] += 1

    for author, score in sorted(author_scores.items()):
        print(author, score)
        

