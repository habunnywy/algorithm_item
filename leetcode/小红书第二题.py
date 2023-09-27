# 读入天数n
n=int(input().strip())
# 依次读取单词列表
words_dict=dict() #单词出现次数
words_rem=[] #已经记住的单词
rem_num=0
for i in range(n):
    word=input().strip()
    if word not in words_dict.keys():
        words_dict[word]=1
    else:
        words_dict[word]+=1
    if word not in words_rem and words_dict[word]>rem_num:
        rem_num+=1
        words_rem.append(word)

print(rem_num)