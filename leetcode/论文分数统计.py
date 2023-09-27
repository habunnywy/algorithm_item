from collections import defaultdict

n = int(input().strip())
author_scores = dict()

for _ in range(n):
    paper_info = input().strip().split()
    author_count = int(paper_info[0])

    # 根据作者顺序，将相应的分数加到字典中
    for i in range(author_count):
        author = paper_info[i + 1]
        if author not in author_scores.keys():
            author_scores[author] = 0
        if i == 0:
            author_scores[author] += 3
        elif i == 1:
            author_scores[author] += 2
        elif i == 2:
            author_scores[author] += 1

# 按照字典序从小到大输出每个作者及其对应的加分总和
for author, score in sorted(author_scores.items()):
    print(author, score)
