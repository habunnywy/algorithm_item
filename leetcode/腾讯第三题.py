#测试数据组数T
import math
T=int(input())

out=[]
for _ in range(T):
    # 读取文章总数D,每篇文章的单词数W，给定的阈值t
    D,W,t=map(float,input().strip().split())
    D=int(D)
    W=int(W)
    # 读取每篇文章的单词
    words=[]
    for i in range(D):
        words.append(input().strip().split())
    # 统计每个单词出现的次数，和包含该词的文章数
    word_count={}
    word_article={}
    word_TFIDF_max=0
    for i in range(D):
        for word in words[i]: #每篇文章的单词
            if word not in word_count:
                word_count[word]=1
                word_article[word]=[i]
            else:
                word_count[word]+=1
                if i not in word_article[word]:
                    word_article[word].append(i)
    for key in word_count:
        word_count[key]=word_count[key]/(D*W)
        word_article[key]=math.log(D/len(word_article[key]))
        word_TFIDF=word_count[key]*word_article[key]
        if word_TFIDF>word_TFIDF_max:
            word_TFIDF_max=word_TFIDF
    if word_TFIDF_max>t:
        out.append(1)
    else:
        out.append(0)
for i in out:
    print(i)