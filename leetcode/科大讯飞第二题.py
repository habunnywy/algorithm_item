# 检测输入字符串是否满足需求
input_s=input().strip()
# 检测长度是否在8到32之间
if not 8<=len(input_s)<=32:
    print("不合格")
    exit()

# 检测首字符是否为大写字符
if not input_s[0].isupper():
    print("不合格")
    exit()

# 检测是否至少包含一个大写字母、一个小写字母、一个数字、一个特殊符号
# 大写字母
upper_flag=False
# 小写字母
lower_flag=False
# 数字
digit_flag=False
# 特殊符号
# 特殊字符列表
special_list=['!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']','|',':',';','"','<','>','?',',','.','/','~','`']
special_flag=False
for char in input_s:
    if char.isupper():
        upper_flag=True
    elif char.islower():
        lower_flag=True
    elif char.isdigit():
        digit_flag=True
    elif char in special_list:
        special_flag=True
if not upper_flag or not lower_flag or not digit_flag or not special_flag:
    print("不合格")
    exit()
# 检测是否不包含空格
if ' ' in input_s:
    print("不合格")
    exit()
print("合格")