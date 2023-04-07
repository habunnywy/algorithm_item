"""
问题：鬼谷子从2~99中选了两个整数，分别将两数之和、两数之积交给庞涓和孙膑。
    庞涓：我虽然不知道这两个数是什么，但是我知道你肯定也不知道这两个数是什么。
    孙膑：那我知道这两个数了。
    庞涓：那我也知道了。
"""
import numpy as np
wait_list=[i for i in range(2,100)]
def is_aAddb_onlyOne(aAddb):
    """
    判断aAddb是否唯一由2~99内两个不相等的数相加而成
    """
    pair_num=0
    for a in range(2,aAddb//2):
        b=aAddb-a
        if b in wait_list:
            pair_num+=1
        if pair_num>1:
            return False
    if pair_num==1:
        return True

def is_ab_onlyOne(ab):
    """
    判断ab是否唯一由2~99内两个不相等的数相乘而成
    """
    pair_num=0
    for a in range(2,int(np.sqrt(ab))+1):
        if ab%a==0 and ab//a in wait_list:
            pair_num+=1
        if pair_num>1:
            return False
    if pair_num==1:
        return True

def condition1(aAddb):
    """
    检查是否 所有构成aAddb的a(+)b,由它们组成的ab的约数对都不唯一
    """
    for a in range(2,aAddb//2):
        b=aAddb-a
        ab=a*b
        if is_ab_onlyOne(ab):
            return False   #存在ab约数对唯一
    return True #所有ab的约数对都不唯一

def condition2(ab):
    """
    检查是否 所有构成ab的a(*)b，由它们构成的aAddb的合数只有一个是唯一的
    """
    for a in range(2,100):
        if ab%a==0:

            b=ab//a  #拆为a,b
            aAddb=a+b
            aAddb_single_num=0
            if is_aAddb_onlyOne(aAddb):
                aAddb_single_num+=1
            if aAddb_single_num>1:
                return False
    return True

def condition22(ab):
    """
        检查是否 所有构成ab的a(*)b，由它们构成的所有aAddb中，只有一个其所有和数对的积的约数对不唯一
    """
    pair_num=0
    for a in range(2,int(np.sqrt(ab))+1):
        if ab%a==0:
            b=ab//a  #拆为a,b
            if b!=a:
                aAddb=a+b
                if condition1(aAddb): #所有可能的a+b的约数对个数均有多个，返回True
                    pair_num+=1
                if pair_num>1: # 只有一个aAddb符合庞涓的条件，孙膑才能判断说自己知道了
                    return False
    if pair_num==1:
        return True
    else:
        return False

def condition3(aAddb):
    '''
    庞涓根据孙膑的话，唯一确定了a和b。即所有a(+)b中，只有一对满足孙膑的条件
    '''
    pair_num=0
    for a in range(2,aAddb//2):
        b=aAddb-a
        ab=a*b
        if condition2(ab) and condition22(ab):
            pair_num+=1
            if pair_num>1:
                return False
    if pair_num==1:
        return True
    else:
        return False

def condition4(aAddb_list,ab_list):
    aAddb_list_new=[]
    ab_list_new=[]

    for aAddb in aAddb_list:
        for a in range(2,aAddb//2):
            b=aAddb-a
            ab=a*b
            if ab in ab_list:
                aAddb_list_new.append(aAddb)
                continue

    for ab in ab_list:
        for a in range(2,int(np.sqrt(ab))+1):
            if ab%a==0:
                b=ab//a
                aAddb=a+b
                if aAddb in aAddb_list:
                    ab_list_new.append(ab)
                    continue
    return aAddb_list_new,ab_list_new

all_sum_1=[]
all_mul_1=[]
# 分别生成两个人的可能拿到的数
for i in range(2,100):
    for j in range(i+1,100):
        if (i+j) not in all_sum_1:
            all_sum_1.append(i+j)
        if i*j not in all_mul_1:
            all_mul_1.append(i*j)


# 两人还未交谈前都猜不出来
all_sum_2=list(filter(lambda x:not is_aAddb_onlyOne(x),all_sum_1))
all_mul_2=list(filter(lambda x:not is_ab_onlyOne(x),all_mul_1))

# 庞涓说的第一句-->因为是从自己的表出发，故简化他的表
all_sum_3=list(filter(lambda x:condition1(x),all_sum_2))

# 孙膑说的第一句-->基于自己的表，从对方角度考虑，得到了唯一答案
all_mul_3=list(filter(lambda x:condition2(x),all_mul_2))
all_mul_4=list(filter(lambda x:condition22(x),all_mul_3))


# 庞涓说的第二句-->基于自己的表，从对方角度考虑，得到了唯一答案
all_sum_4=list(filter(lambda x:condition3(x),all_sum_3))

# 通过对两者的表进行对照，即庞涓的所有可能应该在孙膑表有所体现，反之亦然
all_sum_5,all_mul_5=condition4(all_sum_4,all_mul_4)


print(all_sum_5)
print(all_mul_5)
