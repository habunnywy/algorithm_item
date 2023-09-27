"""
第一行输入的是测试数据组数
对于每组，第一行是输入的科目数量，第二行是科目成绩，第三行是判定值
2

3
66 66 66
90 70 60
4
99 10 60 25
43 49 43
"""


# 中位数判定
def median(subject_score,judge_score):
    # 对成绩进行排序

    if len(subject_score)%2==0:
        # 偶数个
        median=(subject_score[len(subject_score)//2-1]+subject_score[len(subject_score)//2])/2
        # 向下取整
        median=int(median)
    else:
        # 奇数个
        median=subject_score[len(subject_score)//2]
    return median>=judge_score[0]

# 均值判断
def mean(subject_score,judge_score):
    mean=sum(subject_score)/len(subject_score)
    mean=int(mean)
    return mean>=judge_score[1]

# 去掉最高分和最低分后的均值判断
def mean_without_max_min(subject_score,judge_score):
    mean=sum(subject_score[1:-1])/(len(subject_score)-2)
    mean=int(mean)
    return mean>=judge_score[2]

# 测试组数
n=int(input().strip())
scores=[]
judge_scores=[]
for _ in range(n):
    # 对于每组输入数据
    # 科目数量
    subject_num=int(input().strip())
    # 科目成绩
    subject_score=list(map(int,input().strip().split()))
    # 判定值
    judge_score=list(map(int,input().strip().split()))
    scores.append(subject_score)
    judge_scores.append(judge_score)
for _ in range(n):
    subject_score=scores[_]
    judge_score=judge_scores[_]
    # 对subject_score进行排序
    subject_score.sort()
    if median(subject_score,judge_score) and mean(subject_score,judge_score) and mean_without_max_min(subject_score,judge_score):
        print('Yes')
    else:
        print('No')