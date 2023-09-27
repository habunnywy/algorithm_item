"""
假设你是一家大型电商公司的数据科学家，现在你的公司要进行一个营销活动，你需要设计一个推荐系统，来向用户推荐他们可能感兴趣的商品。
你需要实现一个基于协同过滤的推荐算法，编写一个程序，该程序可以读取用户购买历史数据，计算商品之间的相似度，并根据用户的购买历史，推荐他们可能感兴趣的商品。
具体要求如下：
1、程序需要能够读取用户购买历史数据，包含用户ID
2、程序需要计算用户之间或商品之间的相似度，使用余弦相似度计算相似度。
3、程序需要根据用户的购买历史，推荐他们可能感兴趣的商品。程序计算结果四舍五入保留五位小数.喜爱度等于相似度乘以评分.喜爱度大于1的商品是被推荐商品
推荐结果需要包含用户ID和商品ID两列。
4、程序需要包含必要的注释和文档，以便其他人能够理解和使用你的代码。
余弦相似度公式计算商品A和B之间的相似度：<img src="https://uploadfiles.nowcoder.com/images/20230620/0_1687236552222/58A2E5CFF6B2F1115B388175A6F5A73A" alt="">
其中，U表示所有所有购买过商品A或B的用户集合，ru,a表示用户u对a的评分。
余弦相似度的相似值范围是-1到1之间。当两个向量之间的余弦相似度为1时，表示它们的方向完全相同；当余弦相似度为-1时，表示它们的方向完全相反；当余弦相似度为0时，表示它们之间没有任何相似性。
1	A	1
1	B	4.2
2	A	4.5
2	B	2
2	D	3.9
3	A	2.5
3	C	3.8
-1

1	D
2	C
3	B
3	D
"""
import numpy as np

import sys

subject_ID_input=[] #存储出现过的用户ID
suject_ID=[] #存储不重复的用户ID
item_ID_input=[] #存储商品ID
score_input=[] #存储分数

subject_dict=dict() #存储了各用户分别买了哪些
item_dict=dict() #存储各商品所购买的用户和分数

def cos_similarity(item_a,item_b):
    a_id_s=np.asarray(item_dict[item_a])
    b_id_s=np.asarray(item_dict[item_b])
    a_scores=a_id_s[:,-1]
    b_scores=b_id_s[:,-1]
    ru_a2=np.sqrt(np.sum(np.power(a_scores,2)))
    ru_b2=np.sqrt(np.sum(np.power(b_scores,2)))

    ru=0.0
    for sub in a_id_s[:,0]:
        if sub not in b_id_s[:,0]:
            ru+=0
        else:
            temp=a_id_s[np.argwhere(a_id_s[:,0]==sub)[0],1]* \
                b_id_s[np.argwhere(b_id_s[:, 0]==sub)[0],1]
            temp=temp[0]
            ru+=temp

    cos_simi=ru/(ru_a2*ru_b2)
    return cos_simi


for line in sys.stdin:
    a = line.split()
    if len(a)<=1:
        break
    subject_ID_input.append(int(a[0]))
    item_ID_input.append(a[1])
    score_input.append(float(a[2]))

subject_ID=np.unique(np.asarray(subject_ID_input))
#构建商品字典和用户字典，商品字典存储每个商品的购买情况，用户字典存储用户购买过的商品
for i in range(len(item_ID_input)):
    if item_ID_input[i] not in item_dict.keys():
        item_dict[item_ID_input[i]]=[[subject_ID_input[i],score_input[i]]]
    else:
        item_dict[item_ID_input[i]].append([subject_ID_input[i],score_input[i]])
    a=str(subject_ID_input[i])
    if a not in subject_dict.keys():
        subject_dict[a]=[item_ID_input[i]]
    else:
        subject_dict[str(subject_ID_input[i])].append(item_ID_input[i])
#构造商品相似度矩阵
item_ID=list(item_dict.keys())
item_ID.sort()
simi_matrix=np.eye(
    len(item_ID)
                      )
for i in range(len(item_ID)):
    for j in range(len(item_ID)):
        if i==j:
            continue
        simi_matrix[i,j]=cos_similarity(item_ID[i],item_ID[j])

for sub in subject_ID:
    #先找出哪些是sub没买过的商品
    sub_recom=[]
    sub_has_buy=subject_dict[str(sub)]
    for item in sub_has_buy:
        for item_not in item_ID:
            if item_not in sub_has_buy or item_not in sub_recom:
                continue
            # 去找买过的商品中是否有和这个商品喜爱度大于1的
            item_sub_score=item_dict[item]
            sub_index=0
            for i in range(len(item_sub_score)):
                if item_sub_score[i][0]==sub:
                    sub_index=i
                    break
            item_not_index=0
            item_index=0
            for i in range(len(item_ID)):
                if item_ID[i]==item_not:
                    item_not_index=i
                if item_ID[i] == item:
                    item_index = i

            like_score=simi_matrix[item_not_index,item_index]\
                *item_dict[item][sub_index][-1]
            if like_score>1 :
                sub_recom.append(item_not)
    sub_recom.sort()
    for item in sub_recom:
        print("{}\t{}".format(sub,item))