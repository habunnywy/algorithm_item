import sys
# 获取多行输入，直到遇到EOF结束
input_matrix=[]
row_num=0 # 行数
col_maxnum=0 # 列数
per_col_maxnum=[] # 每列中的字符串最大长度
out_str_matrix=[]
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    line_input=line.split(',')
    if len(line_input)>col_maxnum:
        col_maxnum=len(line_input)
    now_col_num=[len(_) for _ in line_input]
    if len(now_col_num)>len(per_col_maxnum):
        per_col_maxnum.extend([0]*(len(now_col_num)-len(per_col_maxnum)))
    for i in range(len(now_col_num)):
        if now_col_num[i]>per_col_maxnum[i]:
            per_col_maxnum[i]=now_col_num[i]

    input_matrix.append(line_input)
    row_num+=1

def table_head():
    head=['+']
    for i in range(col_maxnum):
        head.append('-'*per_col_maxnum[i]+'+')
    # 将head转化为字符串
    head_str=''.join(head)
    return head_str

head_str=table_head()
out_str_matrix.append(head_str)
for i in range(row_num):
    row=['|']
    for j in range(col_maxnum):
        if j<len(input_matrix[i]):
            row.append(' '*(per_col_maxnum[j]-len(input_matrix[i][j]))+input_matrix[i][j]+'|')
        else:
            row.append(' '*per_col_maxnum[j]+'|')
    row_str=''.join(row)
    out_str_matrix.append(row_str)
    out_str_matrix.append(head_str)

for i in range(len(out_str_matrix)):
    print(out_str_matrix[i])